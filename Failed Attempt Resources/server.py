from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'sushi'
#Bootstrap(app)
#db_name = 'GM_Marketing.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name 
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#db = SQLAlchemy(app)



@app.route('/form', methods=['GET','POST'])
def form():
    return render_template('form.html')

@app.route('/addrec', methods = ['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['nameRequesting']
            email = request.form['emailrequesting']
            location = request.form['location']
            date = request.form['dateNeeded']

            with sql.connect("GM_Marketing.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO marketingRequests (nameRequesting, emailRequesting, location, dateNeeded) VALUES (?,?,?,?)", (name, email, location, date))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        
        finally:
            return render_template("result.html",msg = msg)
            con.close()
   
class RequestForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email')
    location = StringField('Property')
    date = StringField('Date Needed')
    submit = SubmitField('Submit')
            

#if __name__ == '__main__':
    app.run(debug=True)

# name = request.form['nameRequesting']
#  if form.validate_on_submit():
#             email = request.form['emailRequesting']
#             location = request.form['property']
#             date = request.form['dateNeeded']
#             record = RequestForm(nameRequesting, emailRequesting, location, dateNeeded)
#             db.session.add(record)
#             db.session.commit()
#             message = 'The form has been submitted'
#             return render_template('form.html', message=message)