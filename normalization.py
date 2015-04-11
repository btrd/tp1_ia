import csv
from operator import itemgetter
import numpy as np

min_r = -1
max_r = 1

def readCSV():
  #fill data with csv 
  with open('iris.csv', 'r') as csvfile:
    iris = csv.reader(csvfile)
    ligne = next(iris)
    for row in iris:
      data.append(row)

def max_min():
  #get max and min
  max0 = float(data[0][0])
  max1 = float(data[0][1])
  max2 = float(data[0][2])
  max3 = float(data[0][3])
  min0 = float(data[0][0])
  min1 = float(data[0][1])
  min2 = float(data[0][2])
  min3 = float(data[0][3])
  for row in data:
    if(float(row[0]) > max0):
      max0 = float(row[0])
    if(float(row[1]) > max1):
      max1 = float(row[1])
    if(float(row[2]) > max2):
      max2 = float(row[2])
    if(float(row[3]) > max3):
      max3 = float(row[3])
    if(float(row[0]) < min0):
      min0 = float(row[0])
    if(float(row[1]) < min1):
      min1 = float(row[1])
    if(float(row[2]) < min2):
      min2 = float(row[2])
    if(float(row[3]) < min3):
      min3 = float(row[3])
    if(row[4] not in names):
      names.append(row[4])
  return max0, max1, max2, max3, min0, min1, min2, min3

def normalize():
  for line in data:
    value = line[0]
    line[0] = ( ( (float(value) - min0) * (max_r - min_r) ) /(max0 - min0)  + min_r )
    value = line[1]
    line[1] = ( ( (float(value) - min1) * (max_r - min_r) ) /(max1 - min1)  + min_r )
    value = line[2]
    line[2] = ( ( (float(value) - min2) * (max_r - min_r) ) /(max2 - min2)  + min_r )
    value = line[3]
    line[3] = ( ( (float(value) - min3) * (max_r - min_r) ) /(max3 - min3)  + min_r )
    currentName = line.pop() #delete last colonne
    for name in names:
      if name == currentName:
        line.append(1)
      else:
        line.append(0)
    print line

def calcArea():
  res = []
  for line in data:
    l = []
    l.append(float(line[2]) * float(line[3]))
    l.append(line[4])
    res.append(l)
  return res

def decile(res):
  tabDec = []
  for i in xrange(1,11):
    line = []
    bound_down = (len(res)/10*i-len(res)/10+1)-1
    bound_up = (len(res)/10*i)-1
    line.append(res[bound_down])
    line.append(res[bound_up])
    setosa = 0.0
    versicolor = 0.0
    virginica = 0.0
    for i in xrange(bound_down,bound_up+1):
      if res[i][1] == "Iris-setosa":
        setosa += 1
      elif res[i][1] == "Iris-versicolor":
        versicolor += 1
      elif res[i][1] == "Iris-virginica":
        virginica += 1
    line.append(setosa/15*100)
    line.append(versicolor/15*100)
    line.append(virginica/15*100)

    print line
    tabDec.append(line)

  return tabDec

if __name__ == "__main__":
  data = []
  names = []
  readCSV()
  #max0, max1, max2, max3, min0, min1, min2, min3 = max_min()
  #normalize()
  res = calcArea()
  res.sort(key=lambda x: x[0])
  decile(res)
