from flask import Flask
app = Flask(__name__)


# index route
@app.route('/')
def hello_world():
    return 'Hello World'
