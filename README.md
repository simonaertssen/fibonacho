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

    curl -GET http://localhost:5000/fibonacci/one/5

Get the fibonacci sequence up to and including the 10th number:

    curl -GET http://localhost:5000/fibonacci/all/10

Get the blacklist:

    curl -GET http://localhost:5000/blacklist

Post the number 10 to the blacklist so that is removed from all future output:

    curl -POST -H "Content-Type: application/json" http://localhost:5000/blacklist -d '{"n": 10}'

Delete the number 10 from the blacklist so that is present in all future output:

    curl -X DELETE -H "Content-Type: application/json" http://localhost:5000/blacklist -d '{"n": 10}'

## Output:
The output for [http://localhost:5000/fibonacci/all/1000](http://localhost:5000/fibonacci/all/1000) is:

    {
    "count": 1000, 
    "limit": 100, 
    "next": "http://localhost:5000/fibonacci/all/1000?start=101&limit=100", 
    "previous": "", 
    "results": {
        "1": 1, 
        ...
        "100": 354224848179261915075
    }, 
    "start": 1
    }

There is a count of 10 numbers, with a limit of 100 per page. The next and previous pages are given by urls in the case that we are querying more than 100 numbers.

## Testing:
Test the application (assuming the venv is activated) with:

    pytest
