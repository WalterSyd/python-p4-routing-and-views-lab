#!/usr/bin/env python3

from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
  # Generate numbers from 0 to the given parameter, exclusive
  numbers = '\n'.join(str(i) for i in range(parameter)) + '\n'
  return Response(numbers, mimetype='text/plain')

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(int(num1) + int(num2))
    elif operation == '-':
        return str(int(num1) - int(num2))   
    elif operation == '*':
        return str(int(num1) * int(num2))
    elif operation == 'div':
        return str(int(num1) / int(num2))
    elif operation == '%':
        return str(int(num1) % int(num2))
    else:
        return "Invalid operation", 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)