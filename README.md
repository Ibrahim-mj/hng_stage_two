# Person API

This is a simple REST API for managing a "person" resource. It allows you to perform basic CRUD operations on a person, including adding, retrieving, updating, and deleting a person.

## Getting Started

This API is live here: https://devibrahim.pythonanywhere.com/api/

To get started and set up this project on your local machine, you'll need to have Python and Django installed on your system. You'll also need to install the required dependencies using pip:
## Setup Instructions

To set up this project on your own system, follow these steps:

1. Clone the repository from GitHub:

    ```shell
   git clone https://github.com/Ibrahim-mj/hng_stage_two.git
   ```
2. Install the required dependencies using:
  ```shell
  pip install -r requirements.txt
  ```
3. Run database migrations:
  ```shell
  python manage.py migrate
  ```
4. Go to `settings.py` and set `DEBUG=True`
5. 
   ```python
   DEBUG = True
   ```
6. Start the development server
  ```shell
  python manage.py runserver 8000
  ```
This will start the development server at `http://127.0.0.1:8000/`
Then go to `http://127.0.0.1:8000/api`

## API Endpoints

The following API endpoints are available:

### `GET /api/`

Retrieves the information of all persons in the database

### `GET /api/<int:pk>`

Retrieves details of a person with the specified ID or primary key.

### `POST /api/`

Adds a new person to the database.

### `PUT /api/<int:pk>`

Updates all the details of an existing person with the specified ID.

### `PATCH /api/<int:pk>`

Updates some of the details of an existing person

### `DELETE /api/<int:pk>`

Deletes a person with the specified ID.

## Request/Response Formats

All requests and responses are in JSON format. Although Django rest framework provides a nice interactive UI for the API. Here are the request and response formats for each endpoint:

### `GET /api/`

**Request format:**
```shell
None
```

**Response format:**
```json
#This can be sorted by name or occupation
{ "name": "John Doe", "age": 30, "email": "johndoe@example.com", "occupation": "Pharmacist" }
{ "name": "John Cole", "age": 50, "email": "johncole@example.com", "occupation": "Backend engineer" }
```

### `GET /api/<int:pk>`

**Request format:**
```shell
None
```

**Response format:**
```json
{ "name": "John Doe", "age": 30, "email": "johndoe@example.com", "occupation": "Pharmacist" }
```
### `POST /api/`

**Request format:**
```json 
{ "name": "John Doe", "age": 30, "email": "johndoe@example.com", "occupation": "Pharmacist" }
```
Note that the name and occupation fields must be strings, the age field must be int and the email must be valid. name or email must not exist in the database prior. else the system rejects the POST, PULL, or PATCH request
**Response format:**

```json
{ "name": "John Doe", "age": 30, "email": "johndoe@example.com", "occupation": "Pharmacist" }
```

### `PUT /api/<int:pk>`

**Request format:**
```json
{ "name": "John Doe", "age": 30, "email": "johndoe@example.com", "occupation": "Pharmacist" }
```

**Response format:**
```json
{ "name": "John Doe", "age": 30, "email": "johndoe@example.com", "occupation": "Pharmacist" }
```


### `DELETE /api/<int:pk>`

**Request format:**
```shell
None
```


**Response format:**
```shell
None
```

## Sample API Usage

You can use an API client like Postman or Insomnia or python request library.


Here are some sample API requests that you can use to test the API using the request library:

```python
import requests

# Set the API endpoint URL
url = 'https://devibrahim.pythonanywhere.com/api/'
# if you are on your local machine:
# url = 'http://127.0.0.1:8000/api'

# Define the data for a new person
data = {
    'name': 'John Doe',
    'age': 30,
    'email': 'johndoe@example.com'
    'occupation': 'Pharmacist'
}

# Send a POST request to create a new person
response = requests.post(url, json=data)

# Print the response status code and content
print(response.status_code)
print(response.json())

# Send a GET request to retrieve the new person
person_id = response.json()['id']
response = requests.get(f'{url}{person_id}/')

# Print the response status code and content
print(response.status_code)
print(response.json())
```
The URL is dynamic enough to accommodate different values of `name` and/or `Occupation`
Example:
`https://devibrahim.pythonanywhere.com/api?name=Abdulwaaliy`
should give a response like this:
```json
{
		"name": "Abdulwaaliy",
		"age": 24,
		"email": "waaliy@api.com",
		"occupation": "pharmacist"
	}
```
Try the same for `occupation`. You can combine the two query parameters with `&`

You can also search the database with either name or occupation.
Example:
`https://devibrahim.pythonanywhere.com/api?search=Abdulwaaliy`
should return the same result as above

## Deployment

To deploy this application from your local machine to a production environment, follow these steps:

1. Set the `DEBUG` setting to `False` in `settings.py`.

2. Set the `ALLOWED_HOSTS` setting to the domain name or IP address of your production server.

3. Install any required dependencies on your production server using pip.
  ```shell
  pip install -r requirements.txt
  ```

4. Set up a production database and configure the `DATABASES` setting in `settings.py` to use the production database.

5. Collect all static files using the `collectstatic` management command:

   ```shell
   python manage.py collectstatic
   ```
6. Set up a web server such as Nginx or Apache to serve the application.

7. Configure the web server to run the application using a WSGI server such as uWSGI or Gunicorn.

As it may heppen with django applications in production, the API interface may not work perfectly. The package `whitenoise` has been used to deal with this and you woulf get it when youu use `pip install`.
The appropriate settings has been done and commented in `MIDDLEWARE` and `STATIC_ROOT` and `STATIC_FILES` are set. You may need to adjuust the `STATIC_ROOT` based on your production server requirements.


## Contributing

If you'd like to contribute to this, just make a pull request.
