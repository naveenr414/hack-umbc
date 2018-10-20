from flask import Flask
app = Flask(__name__)

DEBUG = True

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.debug = DEBUG
    app.run()
    app.run(debug = DEBUG)
