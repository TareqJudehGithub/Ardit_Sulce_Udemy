"""
Pandas library
 - Pandas library is one of the useful library for data analytics.
 - Pandas can extract data using data mining, web scraping, and files like
   json, csv, and excel.
 
 - Installation
 $ pip install pandas


 Jupyter Notebook Library
  - Jupyter Notebook is best use for data exploration, visualization and analysis.

 $ pip install jupyter

 # run jupyter
 $ jupyter notebook
  
   - Jupyter shortcuts
     Ctrl + Enter to execute a cell.
     Alt + Enter to create a new cell.
     Esc to exit from a cell.
     Shift + Enter to move to the next cell.
     Shit + Tab to move to the previous cell.

     Help tab provides more shortcuts.

CSV files
 - CSV stands for comma seperated values.
 - A text files where values are seperated by commas.
 - CSV files can be accessed by Excel applications.

Excel files (xls and xlsx)
 - In order for Python and pandas to be able to read Excel files, we should
   install openpyxl library first, as this is considered as dependency for
   reading Excel files.
   $ pip install openpyxl
 
 - We also need to install another dependency library xlrd, which enables
   us to read old excel files format.
   $ pip install xlrd
  
   $ pandas.read_excel(filename, sheet_name=0)
      sheet_name keyword allows us to specify which sheet we wish to present.

Files with no headers
 - We should include parameter header=None in case the file has no
   header, else the first record will be the header, and will not
   be included in any mathematical operation like mean, sum and count.
 - When including None as a header, sequential numbers (starting from 0)
   are set as columns header instead.
 - Parameter sep= should not be used when including header=None.
      0                1              2                 3    4            5   6
    0  1     3666 21st St  San Francisco          CA 94114  USA      Madeira   8
    1  2   735 Dolores St  San Francisco          CA 94119  USA  Bready Shop  15
    2  3      332 Hill St  San Francisco  California 94114  USA  Super River  25
    3  4     3995 23rd St  San Francisco          CA 94114  USA   Ben's Shop  10
    4  5  1056 Sanchez St  San Francisco        California  USA      Sanchez  12
    5  6  551 Alvarado St  San Francisco          CA 94114  USA   Richvalley  20
 

 - Instead of using header=None parameter, we could manually assign columns
   header:
    data.columns = ['ID', 'Address', 'City', 'Zip', 'Country', 'Customer', 'Emp']
 
Setting index columns
 - Row indexes are manually assigned by pandas.
 - To manually assign indexes headers, we use .set_index('column_name') method.
 - set_index() however, does not modify the original dataset, but it creates a
   new one, so we should assign a new variable in this case.

  $ data.set_index('column_name', inplace=True)

      Address           City               Zip Country     Customer  Emp
    ID
    1    735 Dolores St  San Francisco          CA 94119     USA  Bready Shop   15
    2       332 Hill St  San Francisco  California 94114     USA  Super River   25
    3      3995 23rd St  San Francisco          CA 94114     USA   Ben's Shop   10
    4   1056 Sanchez St  San Francisco        California     USA      Sanchez   12
    5   551 Alvarado St  San Francisco          CA 94114     USA   Richvalley   20
 
 - the drop=False parameter will keep the column selected as index in it's original
   location.
   
     



"""

import pandas

df = pandas.DataFrame(data=[], columns=[])
