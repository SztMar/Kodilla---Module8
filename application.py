from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)
#GET
@app.route('/contact', methods=['GET'])
def contact():
       
    return render_template("kontakt.html")

@app.route('/me', methods=['GET'])
def about_me():
       
    return render_template("O_mnie.html")

#POST
@app.route('/contact', methods=['POST'])
def contact_message():
    
    return request.form 
    
