# Person REST API using django
Using django to create a REST API that makes requests to a Person entity

## Usage

### Starting App
Ensure Docker and Docker compose installed on machine, and run
```
docker-compose up
```

### Admin User

1. To use app, go to link: https://0.0.0.0/8000/admin
    Sign in as admin with credentials

2. As admin, explore API, go to:
    - https://0.0.0.0/8000/people
        - Lists all Person entities in the database, with pagination
        - e.g. ```http://0.0.0.0:8000/people/?limit=2```
    - https://0.0.0.0/8000/people/<username>
        - Lists single Person instance with username <username>
        - e.g. ```http://0.0.0.0:8000/people/user123```
    - https://0.0.0.0/8000/peoplerestricted
        - Lists all Person entities in the database, with pagination and hidden username and password
        - e.g. ```http://0.0.0.0:8000/peoplerestricted/?last_name=Potter&age=13```
3. Create new test user, go to:
    https://0.0.0.0/8000/register
    - This will generate a new authentication token associated with this user
    
### Test User

1. Retrieve user token associated with new user from https://0.0.0.0/8000/admin/authtoken/tokenproxy/

2. Include in header when making API requests

e.g. ```curl -X GET http://0.0.0.0:8000/peoplerestricted/ -H 'Authorization: Token <token>'```

3. Endpoints accessible to users:
    - peoplerestricted/
    - register/


