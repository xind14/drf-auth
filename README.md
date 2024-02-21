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
