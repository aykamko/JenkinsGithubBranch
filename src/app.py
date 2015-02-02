from flask import Flask, request
app = Flask(__name__)
app.debug = True

@app.route('/', methods=['POST'])
def parse_request():
    data = request.data
    return data
