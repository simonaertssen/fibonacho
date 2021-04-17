from flask import Flask, make_response, jsonify, request, abort
from computations import compute_fibonacci
from server_help import validate_input, save_app_state, load_app_state
from server_help import paginate


app = Flask(__name__)

PAGINATION_START = 1
PAGINATION_LIMIT = 100


@app.errorhandler(400)
def bad_request(error):
    """
    Communicate the request was invalid.
    """
    return make_response("Invalid nacho\n", 400)


@app.errorhandler(404)
def not_found(error):
    """
    Communicate the web page was not found.
    """
    return make_response("Nacho not found\n", 404)


@app.errorhandler(405)
def not_allowed(error):
    """
    Communicate the action was not allowed.
    """
    return make_response("To nacho or not to nacho, that is the question\n", 405)


@app.errorhandler(500)
def internal_error(error):
    """
    Communicate an internal error occured.
    """
    return make_response("This nacho is not configured for use in the browser\n", 500)


@app.route("/")
def send_welcome():
    """
    Host the main page.
    """
    return make_response("Welcome to fibonacho.com\n", 200)


@app.route('/fibonacci/<quantity>/<int:n>', methods=['GET'])
def handle_fibonacci_in_url(quantity: str, n: int):
    """
    Receive output quantity ('one' or 'all') and n (which term in the
    fibonacci sequence) directly from the url for ease of interaction.
    Return a list of either one or all fibonacci numbers.
    """
    return communicate_fibonacci(quantity, n)


@app.route('/fibonacci', methods=['GET'])
def handle_fibonacci():
    """
    Receive output quantity ('one' or 'all') and n (which term in the
    fibonacci sequence) from json data. Return a list of either one
    or all fibonacci numbers.
    """
    data = request.get_json()
    return communicate_fibonacci(data['quantity'], data['n'])


def communicate_fibonacci(data_type: str, n: int):
    """
    Wrapped function to deal with multiple input sources.
    """
    n = validate_input(n)
    if data_type == 'one':
        possible_keys = [n]
    elif data_type == 'all':
        possible_keys = range(1, n + 1)
    else:
        abort(400)

    the_blacklist = load_app_state()

    keys = list(set(possible_keys) - set(the_blacklist))
    values = [compute_fibonacci(i) for i in keys]

    start = request.args.get('start', PAGINATION_START)
    limit = request.args.get('limit', PAGINATION_LIMIT)
    url = request.url.rsplit('?', 1)[0]
    return paginate(keys, values, url, start, limit)


@app.route('/blacklist', methods=['GET', 'POST', 'DELETE'])
def blacklist():
    """
    Get the blacklist, or post or delete a number in the blacklist.
    """
    the_blacklist = load_app_state()

    if request.method == 'GET':
        return jsonify(the_blacklist)

    data = request.get_json()
    blacklist_me = data['n']
    blacklist_me = validate_input(blacklist_me)

    if request.method == 'POST':
        if blacklist_me not in the_blacklist:
            the_blacklist.append(blacklist_me)
        else:
            abort(400)
    elif request.method == 'DELETE':
        if blacklist_me in the_blacklist:
            the_blacklist.remove(blacklist_me)
        else:
            abort(400)

    save_app_state(the_blacklist)
    return jsonify(the_blacklist)


if __name__ == '__main__':
    app.run(debug=True)
