import openpyxl
import pandas as pd
import numpy as np
import os
from openpyxl.styles import Font


# Load the workbook
# workbook = openpyxl.load_workbook('6111084_XM_11(1)_6_20230401.xlsx')

# Select the worksheet
# worksheet = workbook['Sheet1']

# Get the value of cell A1
# cell_value = worksheet['A1'].value

# print(cell_value)


# Select the worksheet
# worksheet = workbook['Sheet1']

# Insert a new column at column 3
# worksheet.insert_cols(7)

# Access the seventh column
# seventh_column = list(worksheet.iter_cols(min_col=6, max_col=6))[0]

# Set the font style of the cells in the first column
"""
for cell in seventh_column:
    cell.font = Font(b=True, i=True)
    cell.value = 11;
    
"""

# Save the changes
# workbook.save('6111084_XM_11(1)_6_20230401.xlsx')


###----------------------------------###

df = pd.read_excel('6111084_XM_11(1)_6_20230401.xlsx')

# df.iloc[1:, :] = '2-мөр'


#data = pd.read_csv("6111084_XM_11(1)_6_20230401.xlsx") # dataset
print(df.iloc[:,0:10])


print(df.head(n=3))

df.to_excel('6111084_edited.xlsx', index=False)






