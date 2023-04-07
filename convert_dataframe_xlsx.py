# import pandas as pd
import pandas as pd

# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Data': ['Geeks', 'For', 'geeks', 'is',
							'portal', 'for', 'geeks']})

# Create a Pandas Excel writer
# object using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandasEx.xlsx',
				engine ='xlsxwriter')

# Write a dataframe to the worksheet.
df.to_excel(writer, sheet_name ='Sheet1')

# Close the Pandas Excel writer
# object and output the Excel file.
writer.save()
