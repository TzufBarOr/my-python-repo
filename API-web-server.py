from flask import Flask, redirect, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'DELETE'])
def hello():
    if request.method == 'GET':
        return '<font size=7>My name is Tzuf</font>'
    elif request.method == 'POST':
        return input("what is your name please:")
    print("hello" + hello)


app.run(host="0.0.0.0", port=5001, debug=True)