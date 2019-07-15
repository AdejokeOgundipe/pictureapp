from flask import Flask,render_template
import datetime
app=Flask(__name__)


@app.route('/')
def home():
    
# dictionary 
    ages={"Alice":22, "Bob": 27}
    ages["Chalie"]=30
    ages["Alice"] +=1
    print(ages)


    return "homecoming ..................."

#trying Javascript
@app.route('/Testing')
def Testing():
    return render_template('TEstJs.html')
# functions 
def square(x):
    return (x*x)
    
print(square(5))

for i in range(10):
    print("{} squared is {}".format(i, square(i)))

# classes
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
p=Point(3,5)
print(p.x)
print(p.y)

# to display the user input in the browser via the url e.g localhost/joke
@app.route('/<string:name>')
def anyname(name):
    name=name.capitalize()
    return  f"Hello, {name}!"

# app for is it new year.com

@app.route('/answer')
def answer():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day==1
    return render_template('answer.html',new_year=new_year)

# linking within app pages
#url_for cn be use to link and access other pages from a page



if __name__=='__main__':
    app.run(debug=True)























    