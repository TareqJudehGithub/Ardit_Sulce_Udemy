import os, time
import pandas

"""
Third party modules
 
 - This party Python modules are install separately using Python package
   managers like PIP.
     $ pip install package_name
"""

# we wil install Pandas module in order to extract and manipulate
# data from a csv file.
# $ pip install pandas

def read_csv():
     while True:
          if os.path.exists('./files/temps_today.csv'):
               # read csv file using pandas
               data = pandas.read_csv('./files/temps_today.csv')
               
               # .mean() returns the average for all of the columns.
               # return data.mean()

               # mean([column_name]) returns the average of a specified
               # column
               return data.mean()['st1']
               
          else:
               print('File not found!')     


if __name__ == '__main__':
     print(read_csv())