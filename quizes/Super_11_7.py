#!/usr/bin/python

from scipy.spatial import distance

def euclidean(var1 ,var2):
   return distance.euclidean(var1,var2)
   
def manhattan(var1 ,var2):
   return distance.cityblock(var1,var2)
   
data = [[1,6], [2,4], [3,7], [6,8],[7,1],[8,4]]
labels = [7, 8, 16, 44, 50, 68]

q = [4,2]

for i in range(0, len(data)):
   print ('Euclidean[' + str(i) + '] : ' + str(euclidean(data[i], q)))
   
for i in range(0, len(data)):
   print ('Manhattan[' + str(i) + '] : ' + str(manhattan(data[i], q)))
