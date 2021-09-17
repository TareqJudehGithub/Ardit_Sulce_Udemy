"""
Extracting information, filtering, and slicing dataframes

 1. Using Labeles (column names)
 - for filtering data in dataframes, we use the loc() method.
 - .loc[] method accesses a group of rows and columns by label(s) or a boolean 
   array.
 - .loc[] is primarily label based, but may also be used with a boolean array.
    data.loc["from_cell_row": "to_cell_row", "from_column": "to_column"]
 - IMPORTANT: If a column was assigned as an index, that column cannot be
   specified in "from_column".
  
  Examples:

  # accessing a single row 
  data.loc[0, "ID": "Emp"]
   - 0 is the index number and not the ID
   - cells range: "ID": "Emp" 

   outcome: 
    ID                      1
    Address    735 Dolores St
    City        San Francisco
    Zip              CA 94119
    Country               USA
    Cust          Bready Shop
    Emp                    15
    Name: 0, dtype: object
  
  # accessing a range of rows
  data.loc[0:2, "ID": "Emp"]


 2. Using indexing
  - Filtering data in pandas using indexing is similar to indexing/slicing 
    strings and lists.
  
  Example:
   get me the first three row, but exclude the Emp column from data.txt
   $ data.iloc[0:3 , 0:-1]
"""