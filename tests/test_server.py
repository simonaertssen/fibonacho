import requests
import sys
import os

from src.server_help import save_app_state, load_app_state


# Run these tests with an empty blacklist:
save_app_state([])
assert len(load_app_state()) == 0


# Test the blacklist address:
# Handle inappropriate input:
r = requests.post('http://localhost:5000/blacklist', json={'n': 't'})
assert r.status_code >= 400
r = requests.delete('http://localhost:5000/blacklist', json={'n': 't'})
assert r.status_code >= 400

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


# Test the fibonacci address:
# Handle inappropriate input:
r = requests.get('http://localhost:5000/fibonacci', json={'n': 'test'})
assert r.status_code >= 400
r = requests.get('http://localhost:5000/fibonacci', json={'n': [1, 2, 'a']})
assert r.status_code >= 400

# Test correct input
data = {'n': 0, 'quantity': 'one'}
r = requests.get('http://localhost:5000/fibonacci', json=data)
assert r.json()['results'][str(0)] == 0

data = {'n': 15, 'quantity': 'one'}
r = requests.get('http://localhost:5000/fibonacci', json=data)
assert len(r.json()['results'].values()) == 1

r = requests.post('http://localhost:5000/blacklist', json={'n': 15})
r = requests.get('http://localhost:5000/fibonacci', json=data)
assert len(r.json()['results'].values()) == 0
r = requests.delete('http://localhost:5000/blacklist', json={'n': 15})

data = {'n': 15, 'quantity': 'all'}
r = requests.get('http://localhost:5000/fibonacci', json=data)
assert len(r.json()['results'].values()) == 15


# Test pagination:
n = 100000
data = {'n': n, 'quantity': 'all'}
r = requests.get('http://localhost:5000/fibonacci', json=data)
assert r.json()['count'] == n
assert r.json()['previous'] == ''
assert r.json()['next'] == 'http://localhost:5000/fibonacci?start=101&limit=100'


r = requests.post('http://localhost:5000/blacklist', json={'n': 1})
r = requests.post('http://localhost:5000/blacklist', json={'n': 2})
r = requests.post('http://localhost:5000/blacklist', json={'n': 3})
r = requests.post('http://localhost:5000/blacklist', json={'n': 4})
data = {'n': 5, 'quantity': 'all'}
r = requests.get('http://localhost:5000/fibonacci', json=data)
assert r.json()['count'] == 1
