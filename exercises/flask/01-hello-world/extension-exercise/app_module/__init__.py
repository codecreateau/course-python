# The following initialises `app_module` which can then be imported to other 
# files using `from app_module import app`
from flask import Flask

app = Flask(__name__)

# Import from the file in the directory called `routes.py`
from app_module import routes
