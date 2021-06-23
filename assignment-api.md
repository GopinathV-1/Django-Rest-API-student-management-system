# Assignment API #

This API allows you to create an assignment.

## API Authentication ##

To submit or view an order, you need to Authenticate.

You can login by both ways such as Basic Authentication and Token Authentication.

1. Basic Authentication:
    In postman select basic auth in authorization and provide the provide the username 
and password of the super-user.  

2. Token Authentication:
    
    POST `/api-token-auth/`
    
    The request body needs to be in JSON format and include the following properties:
    - `username` - String
    - `password` - String
    
    Example
    ```
    {
        "username": "Valentin",
        "password": "1234"
    }```

    you will get a token

    Now select headers then, create a key called "Authorization" and a value 
    called "Token yoursuperusertoken"

## Endpoints ##

### List of assignments ###

GET `/viewset/assignment/`

Returns a list of assignments.

### Get a single assignment ###

GET `/viewset/assignment/:assignmentId/`

Retrieve detailed information about a assignment.

### Get a first assignment to complete ###

GET `/viewset/assignment/newest/`

Retrive the first assignment to complete.

### Create an assignment ###

POST `/viewset/assignment/`

The request body needs to be in JSON format and include the following properties:

 - `subject` - String
 - `title` - String - Required
 - `content` - String - Required
 - `staff` - String
 - `due_date` - Date in 'YYYY-MM-DD' 

Example
```
{
    "subject": "Chemistry",
    "title": "Respiration",
    "content": "Draw the respiratory system of Animals",
    "staff": "Mrs. Betty Wiza",
    "due_date": "2021-07-16"
}
```

### Update an assignment ###

PUT `/viewset/assignment/:assignmentId/`


The request body needs to be in JSON format and include the following properties:

 - `subject` - String
 - `title` - String - Required
 - `content` - String - Required
 - `staff` - String
 - `due_date` - Date in 'YYYY-MM-DD' 

Example
```
{
    "subject": "Chemistry",
    "title": "Respiration",
    "content": "Draw the respiratory system of Animals",
    "staff": "Mrs. Betty Wiza",
    "due_date": "2021-07-16"
}
```
### Delete an order ###

DELETE `/viewset/assignment/:assignmentId/`

The request body needs to be empty.
