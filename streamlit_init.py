# importing all required libraries/frameworks
import streamlit as stl
from flask import Flask
import sqlite3
from PIL import Image


img = Image.open("/Users/arhan.sheth/Documents/Codes/DX/Flask/emp_details/dxFactor_logo.jpeg")

# streamlit header elements
stl.image(img, width = 100)
stl.title("Employee Database")

# Prompting user to input employee name
name = stl.text_input("Enter Employee Name", "Type Here...")
if (stl.button("Submit")):
    stl.success("Generating Link...")

# Creating Database
emp_connection = sqlite3.connect("EmployeeData.db")

# initialise cursor
emp_cursor = emp_connection.cursor()
emp_cursor.execute("DROP TABLE IF EXISTS employee_data")

# Creating Table
emp_connection.execute('''CREATE TABLE employee_data(
                       NAME TEXT,
                       POST TEXT,
                       LOCATION TEXT)''')

# Entering database values
emp_connection.execute('''INSERT INTO employee_data VALUES(
                       'Arhan', 'intern', 'ahmedabadapp')''')
emp_connection.execute('''INSERT INTO employee_data VALUES(
                       'Hanav', 'intern', 'ahmedabadapp')''')
emp_connection.execute('''INSERT INTO employee_data VALUES(
                       'Rahul', 'data analyst', 'ahmedabadapp')''')
emp_connection.execute('''INSERT INTO employee_data VALUES(
                       'Pankti', 'data scientist', 'ahmedabadapp')''')


# Initialisting Flask
app = Flask(__name__)
@app.route("/getData/<name>")
def getData(result):
    checker = emp_cursor.execute("SELECT EXISTS(SELECT 1 FROM employee_data WHERE NAME = ?)", (result,))
    if (checker == True):
        final_data = emp_cursor.execute("SELECT * FROM employee_data WHERE NAME = ?", (result,))
        return final_data
    else:
        return "No Data Found"


emp_connection.commit()
emp_cursor.close()
emp_connection.close()

