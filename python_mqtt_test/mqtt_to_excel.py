import xlwt
from xlwt import Workbook
import random
from queue import Queue, Full
import paho.mqtt.client as mqtt
from threading import Thread
import time 
import mlogger as mlogger
import json
import time
import sys, getopt,random
import logging
import mlogger as mlogger
import threading
from command import command_input
import command



q = Queue()   #Create Queue                                    
wb = Workbook()  #Create Workbook
sheet1 = wb.add_sheet('Sheet 1') #Create sheet
#message ="Test"
#global message
#global number
#number = 0

def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))  # Print result
    client.subscribe("MakerIOTopic")
    print("Connected") 


def on_message(client, userdata, msg):
    #global message
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg
    print("payload=",msg.payload)
    msg.payload = msg.payload.decode("utf-8")
    #message = msg.payload
    #print("test2" + message)

def dump_data():
    #global message
    #global number
    try:
        '''
        while True:
            try:
                q.put_nowait(message)
            except Full:
                break
        #take some values from queue
        #print ("Round", i,)
        #number_of_values_to_get = random.randint(0,20)
        #print "getting %i values." % number_of_values_to_get
            for j in range(100):
                value = q.get()
                print ("  got value", message)
                sheet1.write(j, 0, message)
    
        #while True:
            
            q.put_nowait(message)
            message = q.get()
            sheet1.write(number,0,message)
            number = number + 1
            #time.sleep(1)
            '''
     
        message = q.get()
        log.log_data(message)
        #print("message saved ",results["message"])
        #log.close_file()


    except KeyboardInterrupt:
        print ("Exiting")
        log.close_file()

def loop():
    client.loop()



log=mlogger.m_logger("mlogs",5000,0)

client = mqtt.Client("test")  
client.on_connect = on_connect  
client.on_message = on_message 
client.connect('127.0.0.1', 1885)
#print(message)


dataThread = Thread(dump_data())
dataThread.start()

client.q=q

loopThread = Thread(loop())
loopThread.start()


#client.loop_start()

#print(message)

"""
def dump_data():
    global message
    try: 
        while True:
            try:
                q.put_nowait(message)
            except Full:
                break
        #take some values from queue
        #print ("Round", i,)
        #number_of_values_to_get = random.randint(0,20)
        #print "getting %i values." % number_of_values_to_get
        for j in range(100):
            value = q.get()
            print ("  got value", message)
            sheet1.write(j, 0, message)

    except KeyboardInterrupt:
        print ("Exiting")
        wb.save('test5.xls')     

"""


#wb.save('test.xls')



