import requests

# Test the fibonacci address:
data = {'n': 15}
r = requests.get('http://localhost:5000/fibonacci', json=data)
print(r.json())

# Test the blacklist address:
data = {'n': 15}
r = requests.get('http://localhost:5000/blacklist', json=data)
print(r.json())
