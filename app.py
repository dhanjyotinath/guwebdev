from flask import Flask, render_template, request, redirect, url_for
from forms import TestForm
from distutils.log import debug
from fileinput import filename
from flask import *  

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # needed for CSRF

@app.route('/', methods=['GET', 'POST'])
def form_view():
    form = TestForm()
    if form.validate_on_submit():  # True only on valid POST
        return render_template('success.html')
    return render_template('form.html', form=form)

@app.route('/')  
def main():  
    return render_template("index.html")  

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(f.filename)  
        return render_template("Acknowledgement.html", name = f.filename)  


if __name__ == '__main__':
    app.run(debug=True)