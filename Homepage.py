from flask import Flask,render_template,request,url_for,redirect,session, jsonify,flash,send_from_directory,make_response,json
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,form
from wtforms.validators import InputRequired, Email, Length
import pyodbc
import os
from flask_restful import Resource, Api
import base64
from sqlalchemy.ext.declarative import declarative_base
import datetime
from flask_migrate import Migrate
from flask_mail import Mail,Message
from werkzeug.security import generate_password_hash
from flask_login import login_manager,UserMixin,LoginManager
import smtplib

# import modules.flask_login as flask_login
#from flask_login import login_required, UserMixin, current_user,LoginManager

#from models import *

from flask_sqlalchemy import SQLAlchemy


APP_ROOT =os.path.dirname(os.path.abspath(__file__))

# database connection using pyodbc in sql server
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-TN8OFN2\\SQLEXPRESS;"
    "Database=Test;"
    "Trusted_Connection=yes; ")
cursor=conn.cursor()

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mssql+pyodbc://DESKTOP-TN8OFN2\\SQLEXPRESS/test?driver=SQL+Server+Native+Client+11.0'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = smtplib.SMTP('smtp.gmail.com')
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TTL'] =False
app.config['MAIL_USE_SSL'] =True
app.config['MAIL_USERNAME'] ='ogundipeadejoke12@gmail.com'
app.config['MAIL_PASSWORD'] = 'REMIlekun'
# app.config['MAIL_DEFAULT_SENDER'] = 'ogundipeadejoke12@gmail.com'
# app.config['MAIL_MAX_EMAILS']=None
# app.config['MAIL_ASCII_ATTACHMENTS'] = False
# app.config['MAIL_CONNECTION']=True
mail = Mail(app)

db=SQLAlchemy(app)

# secret key assignment
app.config['SECRET_KEY'] = 'mysecretthings'
Bootstrap(app)
api=Api(app)


#UserMixin
class User(UserMixin,db.Model):
    __tablename__='User'
    id= db.Column('id',db.Integer, primary_key=True)
    Name=db.Column(db.String(80))
    Email=db.Column(db.String(80), unique=True)
    Password=db.Column(db.String(128))
    Username=db.Column(db.String(80))
    def __init__(self,Name,Email,Password,Username):
        self.Name = Name
        self.Email=Email
        self.Password=Password
        self.Username=Username 

    def __str__(self):
        return 'Name: {0}, Email: {1} , Username: {2}'.format(self.Name,self.Email,self.Username)
         
# model for Picture
class Picture(db.Model):
    __tablename__='Picture'
    id=db.Column(db.Integer, primary_key=True)
    User_Id = db.Column(db.Integer,db.ForeignKey('user.id'))
    ActualString = db.Column(db.String(80))
    Caption=db.Column(db.String(128))
    def __init__(self,User_Id,ActualString,Caption):
        self.User_Id = User_Id
        self.ActualString=ActualString
        self.Caption=Caption

#model for comment
class Comment(db.Model):
    __tablename__='Comment'
    id=db.Column(db.Integer, primary_key=True)
    Comment=db.Column(db.String(128))
    Picture_Id=db.Column(db.Integer,db.ForeignKey('Comment.PictureId'))
    def __init__(self,comment,Picture_Id):
        self.Comment = Comment
        self.PictureId=Picture_Id
    
#model for likes
class Likes(db.Model):
    __tablename__='Likes'
    id=db.Column(db.Integer, primary_key=True)
    User_Id=db.Column(db.Integer, db.ForeignKey('UserId.Likes'))
    def __init__(self,UserId):
        self.UserId = UserId
 
# def main():
#     user=User(Name="Adejoke",Email="ogundipeadejoke12@gmail.com",username="AARE24", Password="123456789")
  

# to class a new user in sqlalchemy
def main():
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login='login.html'
    login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(id):
#         return User.query.get(int(id))

    
@app.route('/Email')
def EmailAddress():
 #msg=Message('Hello dearie', sender='ogundipeadejoke12@gmail.com',recipients=['ogundipeadejoke12@gmail.com'])
    msg=Message('Hello dearie',sender='ogundipeadejoke121@gmail.com', recipients=['ogundipeadejoke12@gmail.com'])
    print(msg.recipients)
    mail.send_message(msg)
    return "Message sent"
 
#smtplib.SMTPNotSupportedError: SMTP AUTH extension not supported by server.

#class definition for action Login
class loginform(FlaskForm):
    username=StringField('<p style="color:blue" > Username </p>',validators=[InputRequired(),Length(min=4, max=15)])
    password = PasswordField('<p style="color:purple"> Password </p>', validators=[InputRequired(),Length(min=8, max=80)])
    remember = BooleanField('remember me')

# class definition for action Register
class Registrationform(FlaskForm):
    name=StringField('Name',validators=[InputRequired(),Length(min=4, max=80)])
    Email=StringField('Email',validators=[InputRequired(), Email(message='Invalid email'), Length(min=8, max=80)])
    username=StringField('Username',validators=[InputRequired(),Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(),Length(min=8, max=80)])
    
 
# definition of each route in the website
@app.route('/')
def MyWebsite():
     return redirect(url_for('index'))


@app.route('/Users', methods=["GET","POST"])
def Mad():
    if request.method=="POST":
        new_user = User(request.form['Name'],request.form['Email'],request.form['Password'],request.form['username'])
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('Myhome'))
    return render_template('User.html',User=User.query.all())


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/Login', methods=['GET','POST'])
def login():  
    form = loginform(request.form) 
    # session.clear()
   
    if form.validate_on_submit():
     # obtaining data from database
        #cursor.execute('SELECT [Username],[Password] FROM [User] WHERE Username=? AND Password= ?',(form.username.data, form.password.data))
        #new_user= User(request.form['username'],request.form['password'])
       # print(new_user)
        
        username_field = request.form['username']
        password_field = request.form['password']

        user = User.query.filter_by(Username = username_field, Password = password_field).first()

        # print(user)
        # users=User.query.all()
        # print(users)
        user=User.query.filter_by(Email=Email)
        db.session()
        

        if (user is None):
            return "Invalid Username and password <br />"+ "Not yet registered?" + "<a href='/Registration'><br />" +  "click here to Register <br /> </a>" + "to re-login," + "<a href='/Login'><br />" +  "click here to log-in <br /> </a>"
            #return redirect(url_for("login"))
        
        if (user is not None):
            
            session['username'] = request.form['username']
           
            return redirect(url_for('Myhome'))
        
            
        #return "Invalid Username and password <br />"+ "Not yet registered?" + "<a href='/Registration'><br />" +  "click here to Register <br /> </a>" + "to re-login," + "<a href='/Login'><br />" +  "click here to log-in <br /> </a>"
        return redirect(url_for("login"))

    return render_template('login.html',form=form)


# route showing post and get method for registration page
@app.route('/Registration', methods=['GET','POST'])
def Registration():
    form = Registrationform() 
    if form.validate_on_submit():
        # cursor.execute('insert into [User](Name,Email,Password,Username) values (?,?,?,?);',(form.name.data, form.Email.data, form.password.data, form.username.data))
        # cursor.commit()
        # return "Your Registration was successful <br />" + "<a href='/Login'><br />" +  "click here to log in <br /> </a>"
        #reg=User(Name=request.form.get("name"), Email=request.form.get("Email"), Username=request.form.get("username"), Password=request.form.get("password"))
        # print(reg)
        name = request.form.get('name')
        Email=request.form.get('Email')
        Username=request.form.get('username')
        password=request.form.get('password')
       
        user=User.query.filter_by(Email=Email).first()
        if user:
            flash('email address already exists.')  
            return redirect(url_for('Registration'))  
         
            #return "Your Registration was successful <br />" + "<a href='/Login'><br />" +  "click here to log in <br /> </a>"
        new_user = User(Name=name,Email=Email,Username = Username,Password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
  
    return render_template('Registration.html',form=form)

# @app.route('/Registration',methods['POST'])
# def Reg_post():

# dashboard
@app.route('/dashboard',methods=["GET","POST"])
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    return redirect(url_for('login'))


@app.route('/upload',methods=["GET"])
def upload():
    #file=request.files['inputfile']
    return render_template('upload.html') 


@app.route('/upload',methods=["POST"])
def upload_post():
    target = os.path.join(APP_ROOT, 'static\\')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("couldn't create upload directory: {}" .format(target))
   # file = request.files['file']
    for file in request.files.getlist("file"):
        print(file)
        print("{} is the file name". format(file.filename))
        filename= file.filename
        destination = "".join([target, filename])
        print("Accept incoming file", filename)
        print("save it to :", 
        )
        file.save(destination)
        print("filename is : " , filename)
        cursor.execute('''INSERT INTO Picture(
                            
                            UserId,
                             Name,
                             ActualString,
                             Caption) 
                            VALUES(?,?,?,?)''',(1,"Adejoke","images",filename))
        cursor.commit()
        return render_template('dashboard.html', image_name= filename)

    
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory('static',filename)


@app.route('/home')
def Myhome():
    if 'username' in session:
        image_names=os.listdir('./static')
        return render_template('home.html',image_names=image_names)
    return redirect(url_for('index'))
    

@app.route('/test')
def binaryToImage():
    cursor.execute('SELECT [Caption] FROM Picture ')
    my_results= cursor.fetchall()
    image_string = list(my_results)[0][4]
    response = make_response(base64.b64decode(image_string))
    response.headers.set('Content-Type', 'image/jpeg')
    response.headers.set('Content-Disposition', 'attachment', filename = "test.jpg")
    return response
    

@app.route('/return_json', methods=["GET","POST"])
def return_json():
    cursor.execute('SELECT [Caption]  FROM Picture ')
    data = list(cursor.fetchall())
    result = []

    for t in data:
        result.append(os.path.join(APP_ROOT, 'static\\') + t[0])
    
    return jsonify(result)
  
   

@app.route('/About')
def About():
    # if 'username' in session:
    #     return render_template('About.html')
    # else:
    #     return redirect(url_for("login")
    return render_template('About.html')
   

@app.route('/Contact')
def Contact():
    # if 'username' in session:
    #     return render_template('Contact.html')
    # else:
    #     return redirect(url_for("login"))
     return render_template('Contact.html')

@app.route('/logout')
def Logout():
    if 'username' in session:
        session.pop('username',None)
        return redirect(url_for('index'))
    else:
       return redirect(url_for('login'))

@app.route('/Profile')
def profile():
    return render_template('Profile.html')




if __name__ == '__main__':
    app.run(debug=True)
    main()