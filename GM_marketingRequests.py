import sqlite3

#CREATE DATABASE AND
conn = sqlite3.connect('gm_marketing.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE requests (name TEXT, email TEXT, property TEXT, date_needed TEXT)')
print ("Table created successfully")
conn.close()

#WEB VIEWS
from flask import Flask, render_template, request
from wtforms import Form, StringField, validators
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('request.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         email = request.form['email']
         prop = request.form['property']
         date_needed = request.form['date_needed']
         
         with sql.connect("gm_marketing.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO requests (name,email,property,date_needed) VALUES (?,?,?,?)",(name,email,prop,date_needed))
            con.commit()
            msg = "Record successfully added"
            
      except:
          msg = "error in insert operation"
          con.rollback()
        
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("gm_marketing.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from requests")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)









#FAILED ATTEMPTS
# import datetime

# #imports SQLite database for GM Marketing Uniform Inventory
# import sqlite3
# from _sqlite3 import Error
# try: 
#     conn = sqlite3.connect('GM_Marketing.db')
#     print ("Opened Database Successfully!")
# except Exception as e:
#     print("Error durring connection: ", str(e))

# uniform_inventory = conn.execute("SELECT * FROM UNIFORM_INVENTORY")





#Request Form Inputs
# name = input("Name of Individual Requesting Materials: ")
# email = input("Email of Individual Requesting Materials: ")
# date_needed = input("Date Materials are Needed: ")
# #item_needed = 
#property = input("What Property Are These Materials For: ")
# quantity = input("What Quantity Is Needed: ")

#Request Form
# def submit_request ():
#     try:
#         sqliteConnection = sqlite3.connect('GM_Marketing.db')
#         cursor = sqliteConnection.cursor()
#         print("Successfully Connected to SQLite")

#         name = input("Name of Individual Requesting Materials: ")
#         email = input("Email of Individual Requesting Materials: ")
#         date_needed = input("Date Materials are Needed: ")
#         pprt = input("What Property Are These Materials For: ")
        
#         cursor.execute("""INSERT INTO marketingRequests
#                             (nameRequesting, emailRequesting, property, dateNeeded) 
#                             VALUES 
#                             (?,?,?,?)""", (name, email, pprt, date_needed))

#         sqliteConnection.commit()
#         print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
#         cursor.close()

#     except sqlite3.Error as error:
#         print("Failed to insert data into sqlite table", error)
#     finally:
#         if (sqliteConnection):
#             sqliteConnection.close()
#             print("The SQLite connection is closed")

# #view requests
# def view_requests():
#     try: 
#         con = sqlite3.connect('GM_Marketing.db')
#         cur = con.cursor()
#         print("Successfully Connected to SQLite")
#         for row in cur.execute('SELECT * FROM marketingRequests;'):
#             print(row)
#     except Exception as e:
#         print("Error durring connection: ", str(e))


# #menu
# while True:
#     selection = input("What do you want to do?: ")
#     if selection == "1":
#         submit_request()
#     elif selection == "2":
#         view_requests()
#     else:
#         break

#Flask Form
# from flask_wtf import FlaskForm
# from wtforms import StringField, TextField, SubmitField
# from wtforms.validators import DataRequired, Length


# class RequestForm(FlaskForm):
#     """Requrst Form."""
#     name = StringField(
#         'Name',
#         [DataRequired()]
#     )
#     email = StringField(
#         'Email',
#         [
#             Email(message=('Not a valid email address.')),
#             DataRequired()
#         ]
#     )
#     ppty = StringField(
#         'Property',
#         [
#             Email(message=('Not a valid email address.')),
#             DataRequired()
#         ]
#     )
#     date = StringField(
#         'Date Needed',
#         [
#             Email(message=('Not a valid email address.')),
#             DataRequired()
#         ]
   
#     #recaptcha = RecaptchaField()
#     #submit = SubmitField('Submit')

# Flask App
# from flask import (
#     Flask,
#     url_for,
#     render_template,
#     redirect
# )
# from .forms import RequestForm


# app = Flask(__name__, instance_relative_config=False)
# app.config.from_object('config.Config')


# @app.route('/', methods=('GET', 'POST'))
# def request():
#     form = RequestForm()
#     if form.validate_on_submit():
#         return redirect(url_for('success'))
#     return render_template(
#         'index.html',
#         form=form
#     )

#Flask webpage
# from flask import Flask, render_template, request
# app=Flask(__name__)
# @app.route('/greet', methods=['POST'])
# def greet():
#     inputName = request.form['myName']
#     ip = request.remote_addr
#     #write data to file or to DB
#     inputName = inputName.upper()+" hi!  Visiting from " + str(ip)
#     return render_template("home.html",myName=inputName)
# @app.route('/')
# def home():
    
#     return render_template("home.html",myName="")

# if __name__=="__main__":
#     app.run(debug=True)

# for row in uniform_inventory:
#     print (row)

# def insert_data():
#     name_reqursting = input("Enter the name of the person requesting materials: ")
#     email_requesting = input("Enter the email of the person requesting materials: ")
#     location = input ("Enter the item property the materials are needed for: ")
#     date_needed = input("Enter the date needed: ")
#     #changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
#     try:      
#         sqlresult = conn.execute("INSERT INTO marketing_requests (name_requesting,email_requesting,location,date_needed,changemade)\
#             values("+"'"+ str(name_reqursting) +"'" + ",'"+ str(email_requesting) +"', '"+ str(location) +"','"+ str (date_needed))
#         result = conn.commit() #this actually runs the SQL and inserts the data into the database
#         if result == None:
#             print("*** Data saved to database. ***")
#     except Error as e:
#         print ("*** Insert error: ",e)
#         pass

# insert_data()


#Uniform Inventory Items

#GM Mens Polos - Black
# GMP1 = [4,"S","Black","GM Mens Polo"]
# GMP2 = [0,"M","Black","GM Mens Polo"]
# GMP3 = [0,"L","Black","GM Mens Polo"]
# GMP4 = [0,"XL","Black","GM Mens Polo"]
# GMP5 = [6,"XXL","Black","GM Mens Polo"]
# GMP6 = [2,"XXL-Tall","Black","GM Mens Polo"]
# GMP7 = [0,"3XL","Grey","GM Mens Polo"]

#GM Mens Polos - Grey
# GMP8 = [4,"S","Grey","GM Mens Polo"]
# GMP9 = [0,"M","Grey","GM Mens Polo"]
# GMP10 = [0,"L","Grey","GM Mens Polo"]
# GMP11 = [8,"XL","Grey","GM Mens Polo"]
# GMP12 = [0,"XXL","Grey","GM Mens Polo"]
# GMP13 = [0,"XXL-Tall","Grey","GM Mens Polo"]
# GMP14 = [0,"3XL","Grey","GM Mens Polo"]

#GM Womens Polo - Purple
# GMP15 = [8,"S","Purple","GM Womens Polo"]
# GMP16 = [8,"M","Purple","GM Womens Polo"]
# GMP17 = [8,"L","Purple","GM Womens Polo"]
# GMP18 = [6,"XL","Purple","GM Womens Polo"]
# GMP19 = [8,"XXL","Purple","GM Womens Polo"]
# GMP20 = [0,"XXL-Tall","Purple","GM Womens Polo"]
# GMP21 = [0,"3XL","Purple","GM Womens Polo"]

#GM Mens Polo - Purple
# GMP22 = [6,"S","Purple","GM Mens Polo"]
# GMP23 = [0,"M","Purple","GM Mens Polo"]
# GMP24 = [0,"L","Purple","GM Mens Polo"]
# GMP25 = [12,"XL","Purple","GM Mens Polo"]
# GMP26 = [10,"XXL","Purple","GM Mens Polo"]
# GMP27 = [0,"XXL-Tall","Purple","GM Mens Polo"]
# GMP28 = [0,"3XL","Purple","GM Mens Polo"]

#Searches inventory for a secific item, specified by the user
# def search():
#     search_item = input("Enter the Item ID: ")
#     search_quantity = input("Enter Quantity: ")
#     if search_quantity <= search_item.upper()[0]:
#         print("SUCCESS, we have what you are looking for!")
#         request = input("Do you want to submit a request to the marketing department? (Y/N): ")
#         if request.isalpha():
#             if request.lower() == "y":
#                 print(type(search_item[0]))
#                 orig_quant = search_item[0]
#                 search_item[0] = int(orig_quant)-int(search_quantity)
#             else:
#                 pass
#         else:
#             print("Invalid Selection")

#search()
        

# def request(req_avail,req_search_item,req_search_quantity):
#     if req_avail == 1:
#         req_search_item[0] -= req_search_quantity
#     elif req_avail == 0:
#         print("Looks like we are temporarally out of that item.")


   
# def view_inventory():
#     print("GMP1:",GMP1)
#     print("GMP2:",GMP2)
#     print("GMP3:",GMP3)
#     print("GMP4:",GMP4)
#     print("GMP5:",GMP5)
#     print("GMP6:",GMP6)
#     print("GMP7:",GMP7)
#     print("GMP8:",GMP8)
#     print("GMP9:",GMP9)
#     print("GMP10:",GMP10)
#     print("GMP11:",GMP11)
#     print("GMP12:",GMP12)
#     print("GMP13:",GMP13)
#     print("GMP14:",GMP14)
#     print("GMP15:",GMP15)
#     print("GMP16:",GMP16)
#     print("GMP17:",GMP17)
#     print("GMP18:",GMP18)
#     print("GMP19:",GMP19)
#     print("GMP20:",GMP20)
#     print("GMP21:",GMP21)
#     print("GMP22:",GMP22)
#     print("GMP23:",GMP23)
#     print("GMP24:",GMP24)
#     print("GMP25:",GMP25)
#     print("GMP26:",GMP26)
#     print("GMP27:",GMP27)
#     print("GMP28:",GMP28)
