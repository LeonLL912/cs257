from flask import Flask
from flask import render_template
import psycopg2
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    message = "Welcome to My Example Webpage."
    message = message + " This text was produced by concatenating strings in Python!"
    return render_template("homepage.html", someText = message)

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
    return render_template("randborn.html", firstname = firstrowlist[firstnum][0], lastname = lastrowlist[lastnum][0], year = yearrowlist[yearnum][0], city = cityrowlist[citynum][0])

if __name__ == '__main__':
    my_port = 5219
    app.run(host='0.0.0.0', port = my_port) 
