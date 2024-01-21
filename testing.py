from urllib import request
# importing Flask and other modules
from flask import Flask, request, render_template 

import tensorflow as tf
import numpy as np
from termhint import model, tokenized_words, df

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
       
      sentence_to_predict_on = search_text
      num_of_predictions = 10
      prediction = model.predict([sentence_to_predict_on])

      items=[]
      for i, index in enumerate(tf.squeeze(np.argsort(prediction))[::-1][:num_of_predictions]):
        items.append({'id':i+1, 'word':df["Word"][np.where(tokenized_words.numpy() == index)[0][0]].capitalize()})
        
        # THIS GETS YOU PROBABILITY OF GUESS:   tf.squeeze(prediction)[index]*100:.2f
        # THIS GETS YOU THE GUESSED WORD:       df["Word"][np.where(tokenized_words.numpy() == index)[0][0]]
        # THIS GETS YOU THE DEFINITION:         df["Meaning"][np.where(tokenized_words.numpy() == index)[0][0]]
        #print(items)
      print(items)
       #items = [
        #  {'id': 1, 'name': 'boodz'},
        #  {'id': 2, 'name': 'azaan'},
        #  {'id': 3, 'name': 'anz'},
        #]

       #return f"Your name is {first_name} {last_name}, you typed {search_text} <br><a href='/geto/'>Go Back</a>"
    return render_template("anwser.html", anwser=items)

if __name__ == '__main__':
  app.run(debug=True)