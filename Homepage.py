from flask import Flask,render_template,request,url_for,redirect,session, jsonify,flash,send_from_directory,make_response,json
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,form
from wtforms.validators import InputRequired, Email, Length
import pyodbc
import os
from flask_restful import Resource, Api
import base64

APP_ROOT =os.path.dirname(os.path.abspath(__file__))

# database connection using pyodbc 
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-TN8OFN2\\SQLEXPRESS;"
    "Database=Test;"
    "Trusted_Connection=yes; ")
cursor=conn.cursor()
# session assignment
#session['username'] = 'username'
app= Flask(__name__)

# secret key assignment
app.config['SECRET_KEY'] = 'mysecretthings'
Bootstrap(app)
api=Api(app)

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
    
 
# definition of each route in the website
@app.route('/')
def MyWebsite():
     return redirect(url_for('Myhome'))
   

@app.route('/Login', methods=['GET','POST'])
def login():  
    form = loginform(request.form) 
    # session.clear()
   
    if form.validate_on_submit():
     # obtaining data from database
        cursor.execute('SELECT [Username],[Password] FROM [User] WHERE Username=? AND Password= ?',(form.username.data, form.password.data))
        
        if (len(list(cursor))> 0):
            session['username'] = request.form['username']
        
            return redirect(url_for('Myhome'))
        

        return "Invalid Username and password <br />"+ "Not yet registered?" + "<a href='/Registration'><br />" +  "click here to Register <br /> </a>"
       

    return render_template('login.html',form=form)


# route showing post and get method for registration page
@app.route('/Registration', methods=['GET','POST'])
def Registration():
    form = Registrationform() 
    if form.validate_on_submit():
        cursor.execute('insert into [User](Name,Email,Password,Username) values (?,?,?,?);',(form.name.data, form.Email.data, form.password.data, form.username.data))
        cursor.commit()
        # return "Your Registration was successful <br />" + "<a href='/Login'><br />" +  "click here to log in <br /> </a>"
        return redirect(url_for('login'))
  
    return render_template('Registration.html',form=form)


# dashboard
@app.route('/dashboard',methods=["GET","POST"])
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')


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
    return redirect(url_for('login'))
    

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
    if 'username' in session:
        return render_template('About.html')
    else:
        return redirect(url_for("login"))
   

@app.route('/Contact')
def Contact():
    if 'username' in session:
        return render_template('Contact.html')
    else:
        return redirect(url_for("login"))

@app.route('/logout')
def Logout():
    session.pop('username',None)
    return redirect(url_for('login'))

@app.route('/Profile')
def profile():
    return render_template('Profile.html')


if __name__ == '__main__':
    app.run(debug=True)