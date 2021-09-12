import pandas
import os


# df = pandas.read_csv("supermarkets_csv.csv")
# print(df)

# read a file using panda function:
def read_file(file):
     """function that read csv files format"""

     if os.path.exists(file):
          

          # read csv
          if '.csv' in file:
               read_me = pandas.read_csv(file)
               return read_me

          # read json
          elif '.json' in file:
               return pandas.read_json(file)
          
          elif '.xlsx' in file:
               return pandas.read_excel(file, sheet_name=1)
          
          elif '.txt' in file:
               return pandas.read_csv(file, sep=';')
          
          else:
               return 'File format not supported.'

if __name__ == "__main__":
     print(read_file("./supermarkets-semi-colons.txt"))



"""
files:

"supermarkets.json"
"supermarkets_csv.csv"
"supermarkets_xlsx.xlsx"

"""
