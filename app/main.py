from app import app
DEBUG = True

app.debug = DEBUG
app.run(host='127.0.0.1', port=8080, debug=True)
