# Use the Flask app class from `__init__.py` which initialises the `app` and 
# imports this file.
from app_module import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
