import paho.mqtt.client as mqtt
import xlwt
from xlwt import Workbook
import random
from queue import Queue, Full
from datetime import datetime
import subprocess

j = 2
s = 'NA'

q = Queue(100)
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

global s
def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))  
    client.subscribe("MakerIOTopic")  
   

def on_message(client, userdata, msg): 
    global s
    print("Message received-> " + msg.topic + " " + str(msg.payload))  
    s = msg.payload.decode("utf-8")
    print(s)


client = mqtt.Client("digi_mqtt_test")  
client.on_connect = on_connect  
client.on_message = on_message  
print(client.on_message)
client.connect('127.0.0.1', 1885)

"""
try:
    client.loop_forever()  # Start networking daemon
except KeyboardInterrupt:
    print(s)
"""

try:
    sheet1.write(1,0,"Time")
    sheet1.write(1,1,"Vibration")
    while True:
        #global s
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        client.loop()
        print(s)
        sheet1.write(j,1,s)
        sheet1.write(j,0,current_time)
        j = j + 1    
        bashCommand = 'mosquitto_pub -h 127.0.0.1 -t v1/devices/me/telemetry -u 6V5PDTFsqsHc4Wv2X6Qe -m {"TEST":"' + s + '"}'#format(s)
        output = subprocess.check_output(['bash','-c',bashCommand])

except KeyboardInterrupt:
    print("Exiting")
    wb.save('Vibration.xls')


