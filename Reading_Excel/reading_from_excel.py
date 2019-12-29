import pandas as pd

# General Import
data1 = pd.read_excel('readme.xlsx', 'data')

# Fix all nan values
data2 = pd.read_excel('readme.xlsx', 'data')
data2 = data2.fillna('')

# Fix nan values by column
data3 = pd.read_excel('readme_v2.xlsx', 'data')
data3 = data3.fillna({'breed': '', 'puppy': False})

# Fix nan values in specific columns
data4 = pd.read_excel('readme_v2.xlsx', 'data')
data4 = data4.fillna({'breed': ''})

# Fix column data type
data5 = pd.read_excel('readme_v2.xlsx', 'data', dtype={'puppy': bool})
