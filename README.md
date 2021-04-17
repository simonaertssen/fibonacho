# fibonaco
This repository explores the functionality of a RESTful API using the JSON file format. The api can be used to query numbers from the fibonacci sequence, filtered by a blacklist.

## Usage
Clone the repo:

    git clone https://github.com/bonzanini/flask-api-template
    cd flask-api-template

Create virtualenv:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python setup.py develop # or install if you prefer

Run the sample server

    python runserver.py

Try the endpoints:

    curl -XGET http://localhost:5000/dummy
    curl -XPOST -H "Content-Type: application/json" http://localhost:5000/hello -d '{"name": "World"}'

Swagger docs available at `http://localhost:5000/api/spec.html`