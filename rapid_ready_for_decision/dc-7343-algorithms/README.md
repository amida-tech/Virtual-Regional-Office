The `dc-7343-algorithms` directory contains algorithms for determining a claims eligibility for the Rapid Ready for Decision special issue.

This service can be deployed to AWS Lambda or run locally with Flask


# Flask server

To run the app with flask run the following commands from the `rapid_ready_for_decision/dc-7343-algorithms/py-root` directory:

    `export FLASK_APP=py-root/app.py`

    `flask run`


# API Documentation

API documentation is available at
```
http://localhost:5000/apidocs
```

# Docker

Use the commands to build and run with Docker, from the dc-7343-algorithms directory:
`docker build --no-cache -t dc-7343-algorithms .`
`docker run -p 5000:5000 dc-7343-algorithms `