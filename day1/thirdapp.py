
from bottle import route, run, template

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how is goin?', name=name)

run(host='localhost', port=8000, debug=True)