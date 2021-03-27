from flask import Flask, make_response, jsonify, request, abort
from computations import compute_fibonacci
from server_help import validate_input, save_app_state, load_app_state


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    """
    Communicate the web page was not found
    """
    return make_response("Page not found", 404)


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
    data = request.get_json()
    print(data)
    n = data['n']
    n = validate_input(n)

    keys = range(1, n)
    values = [compute_fibonacci(i) for i in keys]
    results = dict(zip(keys, values))
    return jsonify(results)


@app.route('/blacklist', methods=['GET', 'POST', 'DELETE'])
def blacklist():
    """
    Get the blacklist, or post or delete a number in the blacklist
    """
    the_blacklist = load_app_state()

    if request.method == 'GET':
        return jsonify(the_blacklist)

    data = request.get_json()
    blacklist_me = data['blacklist_me']
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
