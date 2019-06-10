# import os
# from flask import Flask,render_template,request
#from flask_dropzone import Dropzone
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
# .L{
#       background-color: blue
#     }
# @app.route('/welcome')
# def welcome():

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

# class PhotoForm(FlaskForm):
#     photo = FileField(validators=[FileRequired()])

# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if form.validate_on_submit():
#         f = form.photo.data
#         filename = secure_filename(f.filename)
#         f.save(os.path.join(
#             app.instance_path, 'photos', filename
#         ))
#         return redirect(url_for('index'))

#     return render_template('upload.html', form=form)
#  <h1> Dashboard</h1>

# <body>
#         <form action ="/" method="POST">
#             <h1> The breaking through</h1>
#         </form>
#     </form>
#     </body> 
#password=sha256_crypt.encrypt(str(form.password.data))
# inserting data into the database 
 #cursor.execute(INSERT INTO ['User'].Picture values (1, (SELECT * FROM OPENROWSET(BULK N'static:\Pt.jpg', SINGLE_BLOB) as Image1)))


# @app.route('/test')
# def binaryToImage():
#     cursor.execute('SELECT [Caption] FROM Picture ')
#     my_results= cursor.fetchall()

#     image_string = list(my_results)[0][4]
    # for pic in my_results:
    #     print(list(pic))
    # file =  open(os.path.join(APP_ROOT, 'static\\') + "testImage.jpg", "wb")
    # file.write(base64.b64decode(image_string))
    # file.close()

    # response = make_response(base64.b64decode(image_string))
    # response.headers.set('Content-Type', 'image/jpeg')
    # response.headers.set('Content-Disposition', 'attachment', filename = "test.jpg")

    # return response
    
#     @app.route('/dashjson', methods=["GET","POST"])
# def dashjson():
    # data = request.get_json()
    # name=data['name']
    # username=data['username']
    # password=data['password']
    # Email=data['Email']
    #return jsonify({'result' : 'success!', 'name' : name, 'username' : username, 'password' : password, 'Email': Email})
    
    # cursor.execute('SELECT [Caption]  FROM Picture ')
    # data = cursor.fetchall()
    # print(data)
    #result=len(list[data])
   
    #image_string = list(data)[1][2]
    # return jsonify({'result :',data})
    # #return jsonify(list(data))
    #return render_template('dashboard.html')
    # print(my_results)
    # return jsonify(data)
      

#dashboard
  #if 'username' in session:
        # cursor.execute('SELECT [Caption],[UserId] FROM Picture')
        # cursor.commit()
        # data = request.get_json()
        # username=data['username']
        # password=data['password']
        # return jsonify({'result' : 'success!',  'username' : username, 'password' : password})
        # result= list(cursor)
        # return jsonify({"key": result})
    #return render_template('dashboard.html') 
    # 
    #  
    # @app.route('api/Users', methods=['GET','POST'])
# def api_User():
#     if request.method='POST':
#         result=request.get_json()
#     else:
#         all_Users={}
#         users=Users.query.all()
 
 
 # return jsonify('Username')
        #api.add_resource('Hello')

         #"You have not logged in <br /> <a href='/Login'><br />" +  "click here to log in <br /> </a>"
    # return render_template('home.html')
     # return jsonify({'student': "ade"})


     #upload
      # destination = "".join([target, filename])
    # print ("Accept incoming file", filename)
    # print ("save it to :", destination)
    
#     @app.route('/upload',methods=["POST"])
# def upload_post():
#     target = os.path.join(APP_ROOT, 'static\\')
#     print(target)
#     try:

#         if  os.path.isdir(target):
#             os.mkdir(target)
#         # else:
#         #     print("couldn't create upload directory: {}".format(target))
#     except:
#         print('just continue please')
#     file = request.files['inputFile']

#     print("{} is the file name".format(file.filename))
#     str = base64.b64encode(file.read())
#     #print(str)
    
#     cursor.execute('''INSERT INTO Picture(
                            
#                             UserId,
#                             Name,
#                             ActualString,
#                             Caption) 
#                             VALUES(?,?,?,?)''',(1,"image","logic",str))
#     cursor.commit()
#     print('saved successfully')

    
#     return redirect(url_for('dashboard'))
    
    # conversion of image to string
    # with open(filePath,"rb") as image:
     # with open("Pk.jpg", "rb") as image:
    #     f = image.read()
    #     b = bytearray(f)
    #     print (b[0])

    #file.save(destination)
    # for converting the string back to image in the sql server

    # cursor.execute('SELECT * FROM Picture')
    # myresults= cursor.fetchall()
    # print(myresults)
    # # converting str back to image
    # img=base64.b85decode(str)
    # return (file.filename)

     # return send_from_directory("static",filename , as_attachment=True)

# @app.route('/upload/<filename>')
# def send_image('filename'):
#     return send_from directory('static',filename)

# @app.route('/home')
# def Myhome():
#     if 'username' in session:
#         # username=session['username']
#         # return 'Logged in as ' + username
       
#         return render_template('home.html')
#     return redirect(url_for('login'))

# for pic in my_results:
    #     print(list(pic))
    # file =  open(os.path.join(APP_ROOT, 'static\\') + "testImage.jpg", "wb")
    # file.write(base64.b64decode(image_string))
    # file.close()
# @app.route('/upload',methods=["GET"])
# def upload():
#     #file=request.files['inputfile']

#     return render_template('upload.html') 

# @app.route('/upload',methods=["POST"])
# def upload_post():
#     target = os.path.join(APP_ROOT, 'static\\')
#     print(target)
#     try:

#         if  os.path.isdir(target):
#             os.mkdir(target)
#         # else:
#         #     print("couldn't create upload directory: {}".format(target))
#     except:
#         print('just continue please')
#     file = request.files['inputFile']

#     print("{} is the file name".format(file.filename))
#     str = base64.b64encode(file.read())
#     #print(str)
#     cursor.execute('''INSERT INTO Picture(
                            
#                             UserId,
#                             Name,
#                             ActualString,
#                             Caption) 
#                             VALUES(?,?,?,?)''',(1,"image","logic",str))
#     cursor.commit()
#     print('saved successfully')

#     # for converting the string back to image in the sql server

#     # cursor.execute('SELECT * FROM Picture')
#     # myresults= cursor.fetchall()
#     # print(myresults)
#     # # converting str back to image
#     # img=base64.b85decode(str)
#     # return (file.filename)
#     return redirect(url_for('dashboard'))
    # return send_from_directory("static",filename , as_attachment=True)

# @app.route('/upload/<filename>')
# def send_image('filename'):
#     return send_from directory('static',filename)







#cursor.execute('INSERT INTO  Picture(UserId,Name,ActualString,Caption) VALUES(?,?,?,?)',(1,"Remmy","img",image_names))
    # cursor.commit()


    # dashboard
# @app.route('/dashboard',methods=["GET","POST"])
# def dashboard():
#     if 'username' in session:
        
    #    cursor.execute('SELECT [Caption] FROM Picture')
    #    results= cursor.fetchall()
    # #    response = make_response(base64.b64decode(results))
    # #result = base64.b64decode(results)
    # # image_string = list(results)[0][0]
    # #print(results)

    # images = []

    # for row in results:
    #     if (row[0] is None):
    #         images.append(None)
    #     else:
    #         images.append(base64.b64encode(row[0]))

    
      
    # return render_template('dashboard.html',images = images)

    #image_names=os.listdir('./static')
    
        #return render_template('dashboard.html')


        #upload
        # @app.route('/upload',methods=["POST"])
# def upload_post():
#     target = os.path.join(APP_ROOT, 'static\\')
#     print(target)
#     try:

#         if  os.path.isdir(target):
#             os.mkdir(target)
#         # else:
#         #     print("couldn't create upload directory: {}".format(target))
#     except:
#         print('just continue please')
#     file = request.files['inputFile']

#     print("{} is the file name".format(file.filename))
#     str = base64.b64encode(file.read())
#     #print(str)
#     cursor.execute('''INSERT INTO Picture(
                            
#                             UserId,
#                             Name,
#                             ActualString,
#                             Caption) 
#                             VALUES(?,?,?,?)''',(1,"image","logic",str))
#     cursor.commit()
#     print('saved successfully')

#     # for converting the string back to image in the sql server

#     # cursor.execute('SELECT * FROM Picture')
#     # myresults= cursor.fetchall()
#     # print(myresults)
#     # # converting str back to image
#     # img=base64.b85decode(str)
#     # return (file.filename)
#     return redirect(url_for('dashboard'))
    # return send_from_directory("static",filename , as_attachment=True)

# @app.route('/upload/<filename>')
# def send_image('filename'):
#     return send_from directory('static',filename)

#filename
#path=base64.b85decode(filename)
     #image_names=os.listdir('./static')
    #newfile= (name=file.filename, data=file.read())
    # images=file.save(os.path.join(('./static'), filename))


    # @app.route('/device')
# def dbCon():
#     if 'username' in session:
        
#         path = base64.b64encode(os.listdir('./static/'))
       
#         cursor.execute('INSERT INTO  Picture(UserId,Name,ActualString,Caption) VALUES(?,?,?,?)',(3,"Remmy","img",path))
#         cursor.commit()
#         return "successful"
#     return ('dashbord.html')
    
    
    
    #return render_template('home.html',image_names=image_names)
     # image_name=os.listdir('./static/')
        # path = base64.b64encode(image_name)


        #print(myresult)
    #print(myresult[0])
    # data= request.get( cursor.execute('SELECT [Caption]  FROM Picture '))
    #print(data)
    # print(json.dumps(data))