import flask

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
    return '<h1 style="background-color:Orange;"> + word1 + </h1> <p style="background-color:AntiqueWhite;">Lorem ipsum...</p>'

if __name__ == '__main__':
    my_port = 5119
    app.run(host='0.0.0.0', port = my_port) 