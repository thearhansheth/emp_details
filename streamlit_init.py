# importing all required libraries/frameworks
import streamlit as stl
from flask import Flask, jsonify
import sqlite3
from PIL import Image
import time

# Creating Database
emp_connection = sqlite3.connect("EmployeeData.db", check_same_thread = False)

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
print("Data Insertion Successul!")

# Initializing Flask
app = Flask(__name__)
@app.route("/getData/<name>")
def getData(name):
        emp_cursor.execute("SELECT * FROM employee_data WHERE NAME = ?", (name,))
        final_data = emp_cursor.fetchall()
        return final_data

img = Image.open("/Users/arhan.sheth/Documents/Codes/DX/Flask/emp_details/dxFactor_logo.jpeg")

# streamlit header elements
stl.image(img, width = 100)
stl.title("Employee Database")

# Prompting user to input employee name
name = stl.text_input("Enter Employee Name", "Type Here...")
if (stl.button("Submit")):
    stl.warning("Generating URL... DO NOT CLOSE")
    time.sleep(5)
    checker = emp_cursor.execute("SELECT EXISTS(SELECT 1 FROM employee_data WHERE NAME = ?)", (name,))
    if name != 'Type Here...':
        stl.success("Link Generated!")
        flask_url = f'http://127.0.0.1:5000/getData/{name}'
        time.sleep(2)
        stl.info(f'Generated URL: {flask_url}')
        app.run(port = 5000)

emp_cursor.close()
emp_connection.close()

