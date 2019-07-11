from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return """This is ssafy !"""

@app.route('/ssafy')
def bye():
    return """This is ssafy !"""



