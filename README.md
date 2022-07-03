# pyforge3

###How to run:

Run the following commands from the root folder.

If you use M1-Based macs:

>export DOCKER_DEFAULT_PLATFORM=linux/amd64
(Ref: https://github.com/psycopg/psycopg2/issues/1360)

Create containers:
>docker-compose build && docker-compose up -d

>docker exec -ti python_app /bin/bash

Run the script to display protein data
>python main.py

#Test
Run tests:
>python -m pytest tests/



