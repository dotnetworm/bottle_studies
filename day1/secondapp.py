from bottle import Bottle, run
app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World again!"

run(app, host='localhost', port=8000)    