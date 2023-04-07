# import pandas library as pd
import pandas as pd

# from datetime module import
# datetime and date method
from datetime import datetime, date

# Create a Pandas dataframe from some datetime data.
# datetime(year,month,date,hour,minute,second)
# date(year,month,date)
dataframe = pd.DataFrame({
	'Date and time': [ datetime(2018, 1, 11, 11, 30, 55),
					datetime(2018, 2, 12, 1, 20, 33),
					datetime(2018, 3, 13, 11, 10 ),
					datetime(2018, 4, 14, 16, 45, 35),
					datetime(2018, 5, 15, 12, 10, 15)],
					
'Dates only': [ date(2018, 6, 21),
					date(2018, 7, 22),
					date(2018, 8, 23),
					date(2018, 9, 24),
					date(2018, 10, 25) ], })

# Create a Pandas Excel writer
# object using XlsxWriter as the engine.
# Also set the default datetime and date formats.

# mmmm dd yyyy => month date year
# month - full name, date - 2 digit, year - 4 digit

# mmm d yyyy hh:mm:ss => month date year hour: minute: second
# month - first 3 letters , date - 1 or 2 digit , year - 4 digit.
writer_object = pd.ExcelWriter("Example_datetime.xlsx",
						engine ='xlsxwriter',
						datetime_format ='mmm d yyyy hh:mm:ss',
						date_format ='mmmm dd yyyy')

# Write a dataframe to the worksheet.
dataframe.to_excel(writer_object, sheet_name ='Sheet1')

# Create xlsxwriter worksheet object
worksheet_object = writer_object.sheets['Sheet1']

# set width of the B and C column
worksheet_object.set_column('B:C', 20)

# Close the Pandas Excel writer
# object and output the Excel file.
writer_object.save()
