# import os
# from flask import Flask,render_template,request
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello World!"

# @app.route('/', methods=["POST"])
# def submit_login():
#     return render_template("home-page.html")

# @app.route('/layout')
# def layout():
#     return render_template("layout.html")

# @app.route('/welcome')
# def welcome():
#     return render_template('welcome.html')

# @app.route('/registration',methods=["POST"])
# def Register():
#     username = request.form.get("username")
#     password = request.form.get("password")

#     if not username or not password:
#          return '<h1>' + form.username.data + ' ' + form.password.data
#     else:
#         return render_template("Registration.html")
# else:
    #     return " Invalid Process"
        # return redirect(url_for('dashboard'))
          # form.username.data + ' ' + form.Email.data + ' ' + form.password.data 
    
#"You have Successfully Registered "
    # cnxn
# from flask_sqlalchemy import SQLALchemy

#from flask_login import login_user, LoginManager, UserMixin
# cursor.execute('insert into [User](Name,Email,Password,Username) values (?,?,?,?);',
# ('Adejoke','ogundipeadejoke','AARE', '123455678'))
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
# db = SQLALchemy(app)
   
# # @app.route('/Register',methods=["POST"])
# # def Register():
#     # error=None
#     # if request.method=='POST':
#     #     if request.method['username'] !='admin' or request.form['password'] !='admin':
#     #         error= 'Invalid credentials. Please try again.'
#     #     else:
#     #          return redirect(url)
           

#     # return render_template('Registration.html')


# @app.route('/UserPage')
# def UserPage():
#     return render_template('UserPage.html')

# #CREATE TABLE MyUsers ( firstname VARCHAR(30) NOT NULL,  lastname VARCHAR(30) NOT NULL)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'MyDB'

# mysql = MySQL(app)
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == "POST":
#         details = request.form
#         firstName = details['fname']
#         lastName = details['lname']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
#         mysql.connection.commit()
#         cur.close()
#         return 'success'
#     return render_template('index.html')

# @app.route('/registration',methods=["POST"])
# def Register():
#     username = request.form.get("username")
#     password = request.form.get("password")

#     if not username or not password:
#         return "check your details"
#     else:
#         return render_template("Registration.html")

# if __name__ == '__main__':
#     app.run(debug=True)


