from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)
#GET
@app.route('/', methods=['GET'])
def hello():
    my_name = "John"   
    return f'Hello, {my_name}!'

@app.route('/blog', methods=['GET'])
def blog_main():
    return f"This is a main blog page"

@app.route('/blog/<id>', methods=['GET']) # can be defined as <int:id>, <float:id>, <string:id>, <path:id> and <uuid:id>. Then following inputs can be delivered in url path: intiger, float, string, path and uid, with exceptions that for numbers (int, float) is positive point numbers and for text (string, path) it accept any text without slash - string, with slash - path. For uuid it accept UUID strings. Without defining the parameters, you can deliver any of them (without error).


def blog(id):
    return f"This is blog entry #{id}"

#POST

@app.route('/message', methods=['POST'])
def post_message():    
    return "OK"

@app.route('/message', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/greeting', methods=['GET', 'POST'])
def greeting():
   if request.method == 'GET':
       print("We received GET")
       return render_template("greeting.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)

       
       return redirect("/")


@app.route("/warehouse")
def warehouse():
    items = ["screwdriver", "hammer", "saw"]
    return render_template("warehouse.html", items=items, errors="Błędy")

@app.route("/warehouse_IF")
def warehouse_if():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("warehouse_if.html", items=items, errors=errors)

@app.route("/warehouse_formatting")
def warehouse_formatting():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("warehouse_formatting.html", items=items, errors=errors)

@app.route("/warehouse_inheritance")
def warehouse_inheritance():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("inheritance.html", items=items, errors=errors)

@app.route("/warehouse_inheritance_input")
def warehouse_inheritance_input():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("inheritance_input.html", items=items, errors=errors)