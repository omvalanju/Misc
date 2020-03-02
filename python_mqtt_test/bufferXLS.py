import xlwt
from xlwt import Workbook
import random
from queue import Queue, Full

q = Queue(100)
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

#for i in range(10):
    #fill queue
while True:
    try:
        q.put_nowait(random.randint(1,10))
    except Full:
        break
    #take some values from queue
#print ("Round", i,)
    #number_of_values_to_get = random.randint(0,20)
    #print "getting %i values." % number_of_values_to_get
for j in range(100):
    value = q.get()
    print ("  got value", value)
    sheet1.write(j, 0, value)


wb.save('test100.xls')

