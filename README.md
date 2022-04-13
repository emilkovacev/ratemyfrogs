# ratemyfrogs

### deployment

1. setup a venv `$ python -m venv venv`
2. install requirements `$ python -m pip install requirements.txt`
3. [setup mongoDB](https://www.mongodb.com/docs/manual/installation/)
4. give permissions to frog image populate script `$ chmod +x populate.sh`
5. populate the database `$ ./populate.sh`
6. run the server `uvicorn server:app`
