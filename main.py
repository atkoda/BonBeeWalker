#using: utf-8
#import psycopg2
from flask import Flask, render_template

#connection = psycopg2.connect(host = "localhost", database = "BonbeeDB", user = "Rabbyrinth", password = "Rabbyrinth")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
