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
    Communicate the request was invalid
    """
    return make_response("Invalid nacho", 400)


@app.errorhandler(404)
def not_found(error):
    """
    Communicate the web page was not found
    """
    return make_response("Nacho not found", 404)


@app.errorhandler(405)
def not_allowed(error):
    """
    Communicate the action was not allowed
    """
    return make_response("To nacho or not to nacho, that is the question", 405)


@app.errorhandler(500)
def internal_error(error):
    """
    Communicate the request was invalid
    """
    return make_response("This nacho is not configured for use in the browser yet", 500)


@app.route("/")
def send_welcome():
    """
    Host the main page
    """
    return make_response("Welcome to fibonacho.com", 200)


@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    """
    Receive n and compute all fibonacci nubers up to and including n
    """
    the_blacklist = load_app_state()

    data = request.get_json()
    n = data['n']
    n = validate_input(n)

    if data['type'] == 'single':
        possible_keys = [n]
    elif data['type'] == 'list':
        possible_keys = range(1, n + 1)
    else:
        abort(400)

    keys = list(set(possible_keys) - set(the_blacklist))
    values = [compute_fibonacci(i) for i in keys]

    start = request.args.get('start', PAGINATION_START)
    limit = request.args.get('limit', PAGINATION_LIMIT)
    url = request.url.rsplit('?', 1)[0]
    return paginate(keys, values, url, start, limit)


@app.route('/blacklist', methods=['GET', 'POST', 'DELETE'])
def blacklist():
    """
    Get the blacklist, or post or delete a number in the blacklist
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
    app.run(debug=False)
