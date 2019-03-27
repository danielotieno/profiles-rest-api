# profiles-rest-api

REST API providing basic functionality for managing profiles using DRF.

## API Endpoints

| EndPoint                   | Functionality                    |
| -------------------------- | -------------------------------- |
| POST api/feed/             | Create a new profile status.     |
| GET  api/feed/             | Fetch all profile status         |
| GET  api/feed/<feed_id>    | Fetch a specific status          |
| PUT  api/feed/<feed_id>    | Updating a specific status       |
| DEL  api/feed/<feed_id>    | Deleting a specific status       |
|                            |
| POST api/profile/          | Create a new profile status.     |
| GET  api/profile/          | Fetch all profile status         |
| GET  api/profile/<feed_id> | Fetch a specific status          |
| PUT  api/profile/<feed_id> | Updating a specific status       |
| DEL  api/profile/<feed_id> | Deleting a specific status       |
|                            |
| POST /signup               | Register a new user              |
| POST /login                | Enables registered user to login |
| POST /logout               | Revoke current user token        |

### Technologies used to build the application

[Python 3.7](https://docs.python.org/3.7/)

[Django](https://www.djangoproject.com/)

[Pylint](https://docs.pylint.org/en/1.6.0/installation.html)

[Django Rest Framework](https://www.django-rest-framework.org/)


#### How should this be manually tested

Fork the repo here [Fork me](https://github.com/danielotieno/profiles-rest-api)

`git clone the forked repo in your machine`

#### Change directory to develop branch

`cd profiles-rest-api`

#### Create a virtual environment

`python3 -m venv venv`

#### Activate the virtual environment

`source venv/bin/activate`

#### Install dependencies

`pip install -r requirements.txt`
`pip install pylint`

#### Then run the command below to start the application

`python manage.py runserver`

#### Copy the following command in your browser

`http://localhost:8000/api/`
