import requests

# Test the fibonacci address:
# Handle inappropriate input:
r = requests.get('http://localhost:5000/fibonacci', json={'n': 'test'})
assert r.status_code == 400
r = requests.get('http://localhost:5000/fibonacci', json={'n': [1, 2, 'a']})
assert r.status_code == 400

# Test correct input
r = requests.get('http://localhost:5000/fibonacci', json={'n': 15})
assert r.status_code == 200


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
