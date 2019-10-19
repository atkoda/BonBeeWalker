#using: utf-8
from flask import Flask, render_template
import psycopg2
app = Flask(__name__)

connection = psycopg2.connect(host = "localhost", database = "bonbee_db", user = "ryoya", password = "zzzxxx0822")

cur = connection.cursor()
cur.execute('SELECT * FROM gundam')
data = cur.fetchall()
cur.close()
connection.close()

@app.route('/')
def hello_world():
    return render_template('index.html', len = len(data), data = data)

if __name__ == "__main__":
    app.run()
