#using: utf-8
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello, Heroku"

# render_template('index.html')

app.run()
