# fibonaco
This repository explores the functionality of a RESTful API using the JSON file format. The api can be used to query numbers from the fibonacci sequence. If desired, numbers can be blacklisted so that these are removed from the query response. The blacklist persists in application state. All GET requests to the fibonacho api support pagination, with a default of 100 numbers.

## Installation
Clone the repo:

    git clone https://github.com/simonaertssen/fibonacho.git
    cd fibonacho

Create virtualenv:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Run the sample server

    python src/server.py

## Usage:
Get the 5th fibonacci number:

    curl -XGET http://localhost:5000/fibonacci/one/5

Get the fibonacci sequence up to and including the 10th number:

    curl -XGET http://localhost:5000/fibonacci/one/5

Get the blacklist, which 

    curl -XGET http://localhost:5000/fibonacci/one/5

## Output:
An example output for <url=http://localhost:5000/fibonacci/one/5> is:
    {
    "count": 1, 
    "limit": 100, 
    "next": "", 
    "previous": "", 
    "results": {
        "5": 5
    }, 
    "start": 1
    }


Try the endpoints:

    curl -XGET http://localhost:5000/dummy
    curl -XPOST -H "Content-Type: application/json" http://localhost:5000/hello -d '{"name": "World"}'

Swagger docs available at `http://localhost:5000/api/spec.html`