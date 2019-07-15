import os
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

project_dir=os.path.dirname(os.path.abspath(__file__
))
database_file = "sqlite:///{}".format(os.path.join(project_dir,"bookingdb"))




app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db= SQLAlchemy(app)





@app.route("/booking", methods=["GET","POST"])
def home():
    if (request=="POST"):
        print(request.form)
   
    return render_template("booking.html")





if __name__=='__main__':
    app.run(debug=True)
    