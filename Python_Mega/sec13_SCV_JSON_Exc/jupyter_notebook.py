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
               # returning data with default header if one was not included
               # data = pandas.read_csv(file, header=None)
               # return data

               data = pandas.read_csv('./data.txt')
               # manual header assignment:
               data.columns = [
                    'ID', 'Address', 'City', 'Zip', 'Country', 'Customer', 'Emp'
               ]
               # manual index assignment:
               
               # we could assign a new variable..
               # data_index = data.set_index('ID')
               # return data_index

               # or add the inplace parameters
               data.set_index('ID', inplace=True)
               return data


          else:
               return 'File format not supported.'
          

def index_labeling():
     data = pandas.read_csv("./data.txt")
     data.columns = [
                    'ID', 'Address', 'City', 'Zip', 'Country', 'Customer', 'Emp'
               ]
     # get me the first and the 2nd rows from data.txt using label slicing
     data_sliced = data.loc[0:1, "ID": "Emp"]
     

     # get me a list of all our customers from data.txt
     data_sliced = data.loc[:, "Customer"]

     # save ur result above in a list
     customers_list = list(data_sliced)

     # return customers_list

     # indexing:
     # get me all customers
     customer_indexing = data.iloc[:, -2]

     # in a list?
     cust_list = list(customer_indexing)
     cust_list.sort()

     # how about in a string format?
     cust_str = " ".join(cust_list)
    

     return cust_str




if __name__ == "__main__":
     # print(read_file("./data.txt"))
     print(index_labeling())


"""
files:

"supermarkets.json"
"supermarkets_csv.csv"
"supermarkets_xlsx.xlsx"

"""
