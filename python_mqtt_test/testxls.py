import paho.mqtt.client as mqtt
import xlwt
from xlwt import Workbook
import random
from queue import Queue, Full
import time

q = Queue()
wb = Workbook()
sheet1 = wb.add_sheet('sheet 1')


#message = ''
#global message

#val = ''
#global val
def on_connect(client, userdata, flags, rc):  
    print("Connected with result code {0}".format(str(rc))) 
    client.subscribe("MakerIOTopic")  


def on_message(client, userdata, msg):
    global message
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg
    message = msg.payload.decode("utf-8")
    print (message)
    val = str(msg.payload)
    q.put_nowait(message)
    print(val)

client = mqtt.Client("digi_mqtt_test")  
client.on_connect = on_connect  
client.on_message = on_message
print(client.on_connect)  
client.connect('127.0.0.1', 1883)

j = 1

while True:
    try:
        client.loop()  # Start networking daemon
        sheet1.write(j,0,message)
        j = j + 1
        #print(message)
        print(j)     
        time.sleep(0.01)
    
    except KeyboardInterrupt:
        print ("Exiting")
        wb.save('test100.xls')
        exit()


