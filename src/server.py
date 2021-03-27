from flask import Flask, make_response

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response("Page not found", 404)


@app.route("/")
def send_welcome():
    return make_response("Welcome to fibonacho.com", 200)


@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    return make_response("Fibonacci", 200)


@app.route('/blacklist', methods=['GET', 'POST', 'DELETE'])
def blacklist():
    return make_response("Blacklist", 200)


if __name__ == '__main__':
    app.run(debug=True)
