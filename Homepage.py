from flask import Flask,render_template,request,url_for,redirect,session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,form
from wtforms.validators import InputRequired, Email, Length
import pyodbc
import os

#password=sha256_crypt.encrypt(str(form.password.data))
# database connection using pyodbc 
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-TN8OFN2\\SQLEXPRESS;"
    "Database=Test;"
    "Trusted_Connection=yes; ")
cursor=conn.cursor()
# session assignment

app= Flask(__name__)
# secret key assignment
app.config['SECRET_KEY'] = 'mysecretthings'

Bootstrap(app)

# class definition for action Login
class loginform(FlaskForm):
    username=StringField('username',validators=[InputRequired(),Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(),Length(min=8, max=80)])
    remember = BooleanField('remember me')

# class definition for action Register
class Registrationform(FlaskForm):
    name=StringField('Name',validators=[InputRequired(),Length(min=4, max=80)])
    Email=StringField('Email',validators=[InputRequired(), Email(message='Invalid email'), Length(min=8, max=80)])
    username=StringField('Username',validators=[InputRequired(),Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(),Length(min=8, max=80)])
    
# session['username'] = 'username'
# definition of each route in the website
@app.route('/')
def MyWebsite():
    return redirect(url_for('Myhome'))


@app.route('/home')
def Myhome():
    if 'username' in session:
        username=session['username']
        return 'Logged in as ' + username
    return redirect(url_for('login'))
    #"You have not logged in <br /> <a href='/Login'><br />" +  "click here to log in <br /> </a>"
    # return render_template('home.html')

@app.route('/Login', methods=['GET','POST'])
def login():  
    form = loginform(request.form) 
    # session.clear()
        
    if form.validate_on_submit():
     # obtaining data from database
        cursor.execute('SELECT [Username],[Password] FROM [User] WHERE Username=? AND Password= ?',(form.username.data, form.password.data))
        
        if (len(list(cursor))> 0):
            session['username'] = request.form['username']
        
            return redirect(url_for('dashboard'))
        

        return "Invalid Username and password <br />"+ " <a href='/Registration'><br />" +  "click here to Register <br /> </a>"
    

    return render_template('login.html',form=form)

    
# route showing post and get method for registration page
@app.route('/Registration', methods=['GET','POST'])
def Registration():
    form = Registrationform() 
    if form.validate_on_submit():
        cursor.execute('insert into [User](Name,Email,Password,Username) values (?,?,?,?);',(form.name.data, form.Email.data, form.password.data, form.username.data))
        cursor.commit()

        return "Your Registration was successful <br /><a href='/Login'><br />" +  "click here to log in <br /> </a>"
  
    return render_template('Registration.html',form=form)


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for("login"))

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/logout')
def Logout():
    session.pop('username',None)
    return redirect(url_for('login'))

@app.route('/Profile')
def profile():
    return render_template('Profile.html')

@app.route('/Home')
def Home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)