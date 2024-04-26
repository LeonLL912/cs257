from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/randtrolling')
def randt():
    return render_template("randtrolling.html")

@app.route('/randborn')
def rand():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="liangl",
        user="liangl",
        password="ruby383expo")

    cur = conn.cursor()

    sqlfirst = "SELECT Firstname FROM nametime"
    sqllast = "SELECT Lastname FROM nametime"
    sqlyear = "SELECT year FROM nametime"
    sqlcity = "SELECT city FROM uspop1k"
    
    cur.execute( sqlfirst )
    firstrowlist = cur.fetchall()

    cur.execute( sqllast )
    lastrowlist = cur.fetchall()

    cur.execute( sqlyear )
    yearrowlist = cur.fetchall()

    cur.execute( sqlcity )
    cityrowlist = cur.fetchall()
    
    firstnum = random.randint(0, 9)
    lastnum = random.randint(0, 9)
    yearnum = random.randint(0,19)
    citynum = random.randint(0,50)
    return render_template("randborn.html", firstname = firstrowlist[firstnum], lastname = lastrowlist[lastnum], year = yearrowlist[yearnum], city = cityrowlist[citynum])


if __name__ == '__main__':
    my_port = 5119
    app.run(host='0.0.0.0', port = my_port) 
