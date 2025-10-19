from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! my name is AGATHOZ :3c'

@app.route('/about')
def about():
    return 'About'
