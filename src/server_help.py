from flask import abort, jsonify
import json


def to_positive_integer(n):
    """
    Make the input an integer and raise an error is there is a negative number
    """
    n = int(n)
    if n < 0:
        raise ValueError
    return n


def validate_input(validate_me):
    """
    Check input for non-allowed tokens and make a positive integer if possible
    """
    try:
        if isinstance(validate_me, str):
            raise TypeError
        validate_me = to_positive_integer(validate_me)
    except (TypeError, ValueError):
        abort(400)
    return validate_me


def save_app_state(the_blacklist: list):
    """
    Save the blacklist to disk as it should persist in application state
    """
    with open('the_blacklist.json', 'w') as f:
        json.dump(the_blacklist, f)


def load_app_state():
    """
    Load the persisted blacklist
    """
    with open('the_blacklist.json', 'r') as f:
        the_blacklist = json.load(f)
    return the_blacklist


def paginate(keys: list, values: list, url: str, start: int, limit: int):
    """
    Create a json object that displays a paginated version of the results teruned
    by the fibonacci computation. The keys and values have been filtered out by the
    blacklist.
    Inspired by https://aviaryan.com/blog/gsoc/paginated-apis-flask
    """
    try:
        start = to_positive_integer(start)
        limit = to_positive_integer(limit)
    except ValueError:
        abort(400)

    print("STart")
    count = len(keys)

    page = {}
    page['start'] = start
    page['limit'] = limit
    page['count'] = count

    if start == 1:
        page['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        page['previous'] = url + f'?start={start_copy}&limit={limit_copy}'

    if start + limit > count:
        page['next'] = ''
    else:
        start_copy = start + limit
        page['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)

    print(page['next'])

    if count == 0:
        page['results'] = {}
    else:
        display_keys = keys[(start - 1):(start - 1 + limit)]
        display_values = values[(start - 1):(start - 1 + limit)]
        page['results'] = dict(zip(display_keys, display_values))
    return jsonify(page)


if __name__ == '__main__':
    the_blacklist = [0, 1, 2]
    save_app_state(the_blacklist)
    print('Blacklist saved')
