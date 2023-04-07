 # Importing required functions
import pandas as pd
from flask import Flask, render_template, request
from fileinput import filename

# Flask constructor
app = Flask(__name__)

# Root endpoint
@app.get('/')
def upload():
	return render_template('upload-excel.html')


@app.post('/view')
def view():

	# Read the File using Flask request
	file = request.files['file']
	# save file in local directory
	file.save(file.filename)

	# Parse the data as a Pandas DataFrame type
	data = pd.read_excel(file)


    # Add a new column with the sum of two columns
    
    data.iloc[:, 18]  = data.iloc[:, 8] + data.iloc[:, 9] 
    
    # Save the updated Excel file
    data.to_excel(file, index=False)

	# Return HTML snippet that will render the table
	return data.to_html()


# Main Driver Function
if __name__ == '__main__':
	# Run the application on the local development server
	app.run(debug=True)
