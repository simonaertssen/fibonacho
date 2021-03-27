import requests
import sys
import os

directory = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(directory, '../src/')))
from server_help import save_app_state, load_app_state

# Run these tests with an empty blacklist:
save_app_state([])
assert len(load_app_state()) == 0

# Test the fibonacci address:
# Handle inappropriate input:
r = requests.get('http://localhost:5000/fibonacci', json={'n': 'test'})
assert r.status_code == 400
r = requests.get('http://localhost:5000/fibonacci', json={'n': [1, 2, 'a']})
assert r.status_code == 400

# Test correct input
data = {'n': 15, 'type': 'single'}
r = requests.get('http://localhost:5000/fibonacci', json=data)
assert len(r.json()) == 1
data = {'n': 15, 'type': 'list'}
r = requests.get('http://localhost:5000/fibonacci', json=data)
assert len(r.json()) == 15


# Test the blacklist address:
# Handle inappropriate input:
r = requests.post('http://localhost:5000/blacklist', json={'n': 't'})
assert r.status_code == 400
r = requests.delete('http://localhost:5000/blacklist', json={'n': 't'})
assert r.status_code == 400

# Test correct input
data = {'n': 15}
r = requests.post('http://localhost:5000/blacklist', json=data)
assert r.status_code == 200
assert len(r.json()) == 1
assert r.json()[0] == 15
r = requests.delete('http://localhost:5000/blacklist', json=data)
assert r.status_code == 200 and len(r.json()) == 0
r = requests.get('http://localhost:5000/blacklist')
assert r.status_code == 200 and len(r.json()) == 0
