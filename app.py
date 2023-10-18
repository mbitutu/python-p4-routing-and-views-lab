#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(string)  # Print to console
    return string  # Display in the browser

@app.route('/count/<int:number>')
def count(number):
    numbers = '\n'.join(str(i) for i in range(1, number + 1))
    return numbers

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Division by zero is not allowed.'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'

    return f'Result: {result}'

if __name__ == '__main__':
    app.run(port=5555)
