# pyforge3

### How to run:

Run the following commands from the root folder.

If you use M1-Based macs:

```sh 
export DOCKER_DEFAULT_PLATFORM=linux/amd64

(Ref: https://github.com/psycopg/psycopg2/issues/1360)
``` 


Create containers:

```sh
 docker-compose build && docker-compose up -d
 ```

```sh
docker exec -ti python_app /bin/bash
 ```

Run the script to display protein data
```sh
python main.py
 ```

# Test
Run tests:
```sh
python -m pytest tests/
 ```


