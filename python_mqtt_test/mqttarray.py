import xlwt
from xlwt import Workbook
import random
from queue import Queue, Full
import paho.mqtt.client as mqtt
from threading import Thread

q = Queue(100)   #Create Queue                                    
wb = Workbook()  #Create Workbook
sheet1 = wb.add_sheet('Sheet 1') #Create sheet
message =""

#Connects to MQTT Server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))  # Print result
    client.subscribe("MakerIOTopic") 


def on_message(client, userdata, msg):
    global message
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg
    print(msg.payload)
    msg.payload = msg.payload.decode("utf-8")
    message = msg.payload
    #print("test2" + message)

    try:
        while True:
            try:
                q.put_nowait(message)

            except Full:
                break

            for j in range(100):
                value = q.get()
                print ("  got value",str(message))
                sheet1.write(j, 0, str(message))
                #wb.save('test3.xls')

    except KeyboardInterrupt:
        print ("exiting")
        wb.save('test3.xls')
        client.disconnect()
        client.loop_stop()


client = mqtt.Client("test")  
client.on_connect = on_connect  
client.on_message = on_message 
client.connect('127.0.0.1', 1883)
#client.loop_start()

def loop():
    client.loop_start()


print(message)

"""msg = subscribe.simple("test", hostname="192.0.0.1:1883")
print(message,'      v')

print ("After Daemon")
print ("OKOK",str(message[]))

try:
    while True:
        try:
            client.loop_stop()
            q.put_nowait(message)
            
        except Full:
            break

        for j in range(100):
            value = q.get()
            #print ("  got value",str(message[]))
            #sheet1.write(j, 0, str(message[]))
            wb.save('test3.xls')

except KeyboardInterrupt:
    print ("exiting")
    wb.save('test3.xls')
    client.disconnect()
    client.loop_stop()
"""
def dump_data():
    while True:
        try:
            #client.loop()
            q.put_nowait(message)
        except Full:
            break

        for j in range(100):
            value = q.get()
            print ("  got value",str(message))
            sheet1.write(j, 0, str(message))
            wb.save('test3.xls')
 
#sheet1.write(j, 0, msg.payload)

#client.loop_forever()

#wb.save('test2.xls')


#clientthread = Thread(target = loop)
#clientthread.start()

datathread = Thread(target = dump_data)
datathread.start()

#savethread = Thread(target = save_data)
#savethread.start()
"""
while True:
    try:
        q.put_nowait(message)
    except Full:
        break
    #take some values from queue
    print ("Round", i,)
    number_of_values_to_get = random.randint(0,20)
    print "getting %i values." % number_of_values_to_get
for j in range(100):
    value = q.get()
    print ("  got value", value)
    sheet1.write(j, 0, value)

"""
#wb.save('test.xls')



