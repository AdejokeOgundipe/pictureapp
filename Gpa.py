from flask import Flask
app= Flask(__name__)


# a program to calculate the cgpa of a student
@app.route("/")
def Home():
    name=input("enter your name")
    matric=input("enter your matric number")
    course_offering=input("enter number of courses offering")
    unit=input("the unit for courses")
    print (name,matric,course_offering,unit)
    return "OOOOOOO"


    
@app.route("/solution")
def soln():
    # the solution is 
    return ("name +matric + course_offering +unit")

if __name__=='__main__':
    app.run(debug=True)