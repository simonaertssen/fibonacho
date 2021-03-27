import requests

# Test the fibonacci address:
r = requests.get('http://localhost:5000/fibonacci')

# Test the blacklist address:
r = requests.get('http://localhost:5000/blacklist')
