from flask import *
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "ThisIsASecretKey"
debug = DebugToolbarExtension(app)

RESPONSES = []

@app.route('/')
