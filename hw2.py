"""
Columbia W4111 Intro to databases
Homework 2
"""

import sys
from collections import *


def load_data(file_path):
  """
  This method reads the dataset, and returns a list of rows.
  Each row is a list containing the values in each column.
  """
  import csv
  with file(file_path) as f:
    dialect = csv.Sniffer().sniff(f.read(2048))
    f.seek(0)
    reader = csv.reader(f, dialect)
    return [l for l in reader]


def q1(data):
  """
  @param data the output of load_data()
  @return the number of  distinct types of items (by `description` attribute) in this dataset
  """
  set_description = []
  uniques = []
  for row in data:
    for i in range(21):
        if(i==15):
             set_description.append(row[i])
            
            
  myset = set(set_description)
    
  # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)
  return len(myset) -1

def q2(data):
  """
  @param data the output of load_data()
  @return the number of  distinct `vendor`s (by exact string comparison) in this dataset
  """
  set_description = []
  uniques = []
  for row in data:
    for i in range(21):
        if(i==13):
             set_description.append(row[i])
            
            
  myset = set(set_description)
  
  # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)
  return len(myset)-1

def q3(data):
  """
  @param data the output of load_data()
  @return the value of the `store` attribute (the id) of the store that had the most sales (as defined by bottle qty)
  """
  d = {}
  store = -1
  for row in data[1:]:
    for i in range(21):
        if(i==2):
            if(row[i] in d):
              d[row[i]] = { (d[row[i]]).pop()  + int(row[20])}
            else:
              d[row[i]] = {int(row[20])}
              store = row[i]
            

 

  for k in d.keys():
    if( list(d[k])[0] >= list(d[store])[0]):
      store = k
              
  
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html
  return int(store)

def q4(data):
  """
  @param data the output of load_data()
  @return The value of the `description` attribute of the most sold item from the store from q3()
  """
  d2 = {}
  store = q3(data)
  description = ''
  for row in data[1:]:
    for i in range(21):
        if(i==2 and int(row[i]) == int(store)):
            if(row[15] in d2):
              d2[row[15]] = { (d2[row[15]]).pop()  + int(row[20])}
            else:
              d2[row[15]] = {int(row[20])}
              description = row[15]
            

 

  for k in d2.keys():
    if( list(d2[k])[0] >= list(d2[description])[0]):
      description = k
      
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html
  return description

def q5(data):
  """
  Finds the `zipcode` that has the greatest total `bottle_qty` for `category_name` "TEQUILA"
  @param data the output of load_data()
  @return The value of the `zipcode` attribute with the most sales in "TEQUILA" category
  """
  d1 = {}
  store = -2
  for row in data[1:]:
    for i in range(21):
        if(i==11 and row[i] == 'TEQUILA'):
            if(row[6] in d1):
              d1[row[6]] = { (d1[row[6]]).pop()  + int(row[20])}
            else:
              d1[row[6]] = {int(row[20])}
              store = row[6]
            

 

  for k in d1.keys():
    if( list(d1[k])[0] >= list(d1[store])[0]):
      store = k
      
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html

  return store

if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.stderr.write("Usage: python hw2.py (path to input csv)\n")
    sys.exit(1)
  file_path = sys.argv[1]

  data = load_data(file_path)
  #data = load_data('iowa-liquor-sample.csv')
  print q1(data)
  print q2(data)
  print q3(data)
  print q4(data)
  print q5(data)
