from flask import Flask

# Create a new `Flask` class which has the same name as file being executed
# which is expressed by `__name__`
app = Flask(__name__)

# Register the index function with both `/` and `/index` routes. This can be
# accessed from `http://localhost:5000/` or `http://localhost:5000/index`.
#
# Read the following article for more information
# https://medium.com/@nguyenkims/python-decorator-and-flask-3954dd186cda
@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"
