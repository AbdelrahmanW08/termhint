from urllib import request

# importing Flask and other modules
from flask import Flask, request, render_template 

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')

  return " Click \n <br><a href='/geto/'>Go Back</a>"

# A decorator used to tell the application
# which URL is associated function
@app.route('/geto/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       search_text = request.form.get("txt")
       print (search_text)
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       #return "Your name is "+first_name + last_name
       #return f"Your name is {first_name} {last_name}, you typed {search_text} <br><a href='/geto/'>Go Back</a>"
    return render_template("anwser.html", anwser=search_text)

if __name__ == '__main__':
  app.run(debug=True)