from flask import Flask, make_response, jsonify
from computations import compute_fibonacci

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response("Page not found", 404)


@app.route("/")
def send_welcome():
    return make_response("Welcome to fibonacho.com", 200)


@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    n = 15
    keys = range(1, n)
    values = [compute_fibonacci(i) for i in keys]
    results = dict(zip(keys, values))
    return jsonify(results)


@app.route('/blacklist', methods=['GET', 'POST', 'DELETE'])
def blacklist():
    blacklist = [1, 2, 3, 4]
    return jsonify(blacklist)


if __name__ == '__main__':
    print("App started")
    app.run(debug=True)
