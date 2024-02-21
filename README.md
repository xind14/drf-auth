# Lab: Class 33 - Authentication & Production Server

## Author: Xin Deng

### Links and Resources

- chatGPT
- [Class 33 Demo](https://github.com/codefellows/seattle-code-python-401d24/tree/main/class-33/demo)

### Overview - Django Permissions & Postgresql

This is a project building upon the Django REST Framework to create an API, then “containerize” it with Docker by adding project’s permissions so that only authenticated user’s have access to API and adding a custom permission so that only appropriate users can update or delete it. Moving the API closer to production grade by adding Authentication and switching to a Production Server.




#### Version 1.0

Build 1.0 Feature Tasks

1. Create custom version of Things API demo
2. Create a model and add to admin
3. Model should have as many fields as the demo
4. Model should have one foreign key
5. Implement Docker
6. Define permissions
7. Add JWT Authentication
8. Implement gunicorn

### How to Initialize/Run Application

- `docker-compose up --build`

### How to Run Tests with Thunder Client

#### Get Tokens:

- **Route:** `http://localhost:8000/api/token/`
- **HTTP Method:** POST
- **Token Required:** No

**Steps:**
1. Create a new request in Thunder Client.
2. Set the request URL to `http://localhost:8000/api/token/`.
3. Set the request method to `POST`.
4. In the request body, add:
   ```json
   {
       "username": "admin",
       "password": "admin"
   }
   ```
5. Send the request.

#### Refresh Tokens:

- **Route:** `http://localhost:8000/api/token/refresh/`
- **HTTP Method:** POST
- **Token Required:** Yes (Refresh Token)

**Steps:**
1. Set the request URL to `http://localhost:8000/api/token/refresh/`.
2. Set the request method to `POST`.
3. In the request body, add:
   ```json
   {
       "refresh": "{{refresh_token}}"
   }
   ```
4. Send the request.


#### List All Snack List:

- **Route:** ` http://localhost:8000/api/v1/snacks/`
- **HTTP Method:** GET
- **Token Required:** Yes (Access Token)

**Steps:**
1. Set the request URL to `http://localhost:8000/api/v1/snacks/`
2. Set the request method to `GET`.
3. Add the Authorization header with the value `Bearer {{access_token}}`.
   - Replace `{{access_token}}` with an actual access token.
4. Send the request.

#### Create:

- **Route:** `http://localhost:8000/api/v1/snacks/`
- **HTTP Method:** POST
- **Token Required:** Yes (Access Token)

- **Steps:**
1. Set the request URL to `http://localhost:8000/api/v1/snacks/`.
2. Set the request method to `POST`.
3. Add the Authorization header with the value `Bearer {{access_token}}`.
   - Replace `{{access_token}}` with an actual access token.
4. In the request body, add the data for the new snack.
5. Send the request.

#### Update:

- **Route:** `http://localhost:8000/api/v1/snacks/id/`
- **HTTP Method:** PUT
- **Token Required:** Yes (Access Token)

**Steps:**
1. Set the request URL to `http://localhost:8000/api/v1/snacks/id/`.
   - Replace ID of the resource you want to update.
2. Set the request method to `PUT`.
3. Add the Authorization header with the value `Bearer {{access_token}}`.
   - Replace `{{access_token}}` with an actual access token.
4. In the request body, add the updated data for the resource.
5. Send the request.

#### Delete:

- **Route:** `http://localhost:8000/api/v1/snacks/id/`
- **HTTP Method:** DELETE
- **Token Required:** Yes (Access Token)

**Steps:**
1. Set the request URL to `http://localhost:8000/api/v1/snacks/id/`.
   - Replace ID of the resource you want to delete.
2. Set the request method to `DELETE`.
3. Add the Authorization header with the value `Bearer {{access_token}}`.
   - Replace `{{access_token}}` with an actual access token.
4. Send the request.

