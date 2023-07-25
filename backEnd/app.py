from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

"""
Here's what this code does:
It first imports the Flask module and creates a Flask web server from the Flask module.
@app.route('/') is a Python decorator that Flask provides to assign URLs in our app to functions easily. 
This decorator is telling Flask what to display at which point. So, when we try to reach our web server at 'http://localhost:5000/', it will trigger the home() function and return "Hello, World!"

The if __name__ == '__main__': condition ensures the server only runs if the script 
is executed directly (i.e., it's not imported as a module in a different script).

app.run(debug=True) will start the server and keep it running in debug mode, 
which means Flask will give you detailed error messages if something goes wrong. 
The server will also automatically reload if you make changes to your script.

Save this script in a file (for example, app.py), then run it with Python while your virtual environment is activated:"""