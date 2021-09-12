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

 
     



"""

import pandas

df = pandas.DataFrame(data=[], columns=[])
