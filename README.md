# Lab: Class 33 - Authentication & Production Server

## Author: Xin Deng

### Links and Resources

- chatGPT
- [Class 32 Demo](https://github.com/codefellows/seattle-code-python-401d24/tree/main/class-32/demo)

### Overview - Django Permissions & Postgresql

This is a project building upon the Django REST Framework to create an API, then “containerize” it with Docker by adding project’s permissions so that only authenticated user’s have access to API and adding a custom permission so that only appropriate users can update or delete it.




#### Version 1.0

Build 1.0 Feature Tasks

1. Create custom version of Things API demo
2. Create a model and add to admin
3. Model should have as many fields as the demo
4. Model should have one foreign key
5. Implement Docker
6. Switch to using postgres vs sqlite
7. Define permissions


### How to Initialize/Run Application

- `docker-compose up --build`

#### How to Run Tests

- `docker compose run web python manage.py test`



### Testing Endpoints with Thunder Client:

#### 1. Install Thunder Client:
If you haven't installed Thunder Client in Visual Studio Code, you can install it from the Extensions Marketplace.

### Get Tokens:
**Route:** `POST: http://localhost:8000/api/token/`
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
6. You should receive a response with the access token and refresh token.

### Refresh Tokens:
**Route:** `POST: http://localhost:8000/api/token/refresh/`
- **HTTP Method:** POST
- **Token Required:** Yes (Refresh Token)

**Steps:**
1. Create a new request in Thunder Client.
2. Set the request URL to `http://localhost:8000/api/token/refresh/`.
3. Set the request method to `POST`.
4. In the request body, add:
   ```json
   {
       "refresh": "{{refresh_token}}"
   }
   ```
5. Send the request.
6. You should receive a response with a new access token.


#### List All Resources:
**Route:** `GET: http://localhost:8000/api/v1/snacks/`
- **HTTP Method:** GET
- **Token Required:** Yes (Access Token)

**Steps:**
1. Create a new request in Thunder Client.
2. Set the request URL to `http://localhost:8000/api/v1/snacks/`.
3. Set the request method to `GET`.
4. Add the Authorization header with the value `Bearer {{access_token}}`.
   - Replace `{{access_token}}` with an actual access token.
5. Send the request.

#### Create a New Resource:
**Route:** `POST: http://localhost:8000/api/v1/snacks/`
- **HTTP Method:** POST
- **Token Required:** Yes (Access Token)

**Steps:**
1. Create a new request in Thunder Client.
2. Set the request URL to `http://localhost:8000/api/v1/snacks/`.
3. Set the request method to `POST`.
4. Add the Authorization header with the value `Bearer {{access_token}}`.
   - Replace `{{access_token}}` with an actual access token.
5. In the request body, add the data for the new resource.
6. Send the request.

#### Update an Existing Resource:
**Route:** `PUT http://localhost:8000/api/v1/snacks/id/`
- **HTTP Method:** PUT
- **Token Required:** Yes (Access Token)

**Steps:**
1. Create a new request in Thunder Client.
2. Set the request URL to `http://localhost:8000/api/v1/snacks/id/`.
   - Replace `<resource_id>` with the ID of the resource you want to update.
3. Set the request method to `PUT`.
4. Add the Authorization header with the value `Bearer {{access_token}}`.
   - Replace `{{access_token}}` with an actual access token.
5. In the request body, add the updated data for the resource.
6. Send the request.

#### Delete an Existing Resource:
**Route:** `DELETE: http://localhost:8000/api/v1/snacks/id/`
- **HTTP Method:** DELETE
- **Token Required:** Yes (Access Token)

**Steps:**
1. Create a new request in Thunder Client.
2. Set the request URL to `http://localhost:8000/api/v1/snacks/id/`.
   - Replace `<resource_id>` with the ID of the resource you want to delete.
3. Set the request method to `DELETE`.
4. Add the Authorization header with the value `Bearer {{access_token}}`.
   - Replace `{{access_token}}` with an actual access token.
5. Send the request.

