import flask
import psycopg2

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Welcome to my page hehe!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="background-color:Orange;">' + word1 + '</h1> <p style="background-color:AntiqueWhite;">Lorem ipsum...</p>'


@app.route('/add/<num1>/<num2>')
def my_add(num1, num2):
    result = int(num1) + int(num2)
    the_string = num1 + "+" + num2 + "=" + str(result);
    return the_string

@app.route('/pop/<statename>')
def test_query_all_5(statename):   
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="liangl",
        user="liangl",
        password="ruby383expo")

    cur = conn.cursor()
    sql = "SELECT pop FROM uspop WHERE code = %s"
    
    cur.execute( sql, [statename]  )

    # fetchall() returns a list containing all rows that matches your query
    row_list = cur.fetchall()

    # It is often useful to loop through all rows in a query result
    totalpop = 0
    for row in row_list:
        totalpop += row[0]

    if (totalpop == 0):
        return statename + "does not exist in this database."
    else:
        return "Total population in" + statename + "is:" + str(totalpop)

if __name__ == '__main__':
    my_port = 5119
    app.run(host='0.0.0.0', port = my_port) 