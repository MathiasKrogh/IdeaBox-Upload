"""Creates a web site with activity examples"""
import os.path
import pyrebase
from flask import Flask, render_template, url_for, request

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

firebaseConfig={"apiKey": "AIzaSyC35JQhDJu6JpPUh5UelWToZPa-g3dnlJ4",
  "authDomain": "idea-box-ef8e8.firebaseapp.com",
  "databaseURL": "https://idea-box-ef8e8-default-rtdb.europe-west1.firebasedatabase.app/",
  "projectId": "idea-box-ef8e8",
  "storageBucket": "idea-box-ef8e8.appspot.com",
  "messagingSenderId": "186666334977",
  "appId": "1:186666334977:web:5734a65add2707495d3900",
  "measurementId": "G-Y4SE07Y0TJ"}

# Use the application default credentials
firebase=pyrebase.initialize_app(firebaseConfig)

firedb=firebase.database()

@app.route('/')
@app.route('/home')
def homepage():
    """
    Returns html-template and prints a random activity
    """
    return render_template('main.html')

@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]
    print(output)
    firedb.child("activities").push(output)
    return render_template('main.html', name = name)

if __name__ == "__main__":
    app.run(debug=True)

