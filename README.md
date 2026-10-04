# Book API

A small HTTP service that provides information about books.

## Features

The API provides the following endpoints:

* `GET /` — returns a welcome message
* `GET /healthz` — checks whether the service is running
* `GET /books` — returns a list of books
* `GET /books/<id>` — returns information about one book

## Requirements

* Python 3
* Flask
* pytest
* requests

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the application

Run:

```bash
./scripts/run.sh
```

The default port is `8080`.

A different port can be specified using the `PORT` environment variable:

```bash
PORT=5000 ./scripts/run.sh
```

## Testing

Make sure the application is running, then execute:

```bash
./scripts/test.sh
```

The tests check the main API endpoints and verify that the service returns the expected responses.

