from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def main():
    if request.method == 'GET':
        return render_template('main.html')

@app.route('/kontakt')
def kontakt():
    if request.method == 'GET':
        return render_template('kontakt.html')

@app.route('/o_mnie')
def o_mnie():
    if request.method == 'GET':
        return render_template('o_mnie.html')

from flask import render_template

@app.route('/kontakt', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")
message
main
kontakt
o_mnie