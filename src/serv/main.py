import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def render_form():
    return render_template('form.html')

@app.route("/", methods=['POST'])
def get_form():
    url = request.form['text']
    return url

if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))