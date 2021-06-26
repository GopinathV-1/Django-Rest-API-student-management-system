# Dataproject Django-rest-framework

A project using the django rest framework

This repo consists of a source code of a python script to make an interactive student management system
using **Django rest framework**

## How is it done?

You might be wondering that how the application performs many operations like creation, deletion, and update of assignments. Well, it was not that complicated as you may think. All these were achieved with the help of Database operation. 

We all know that computers can store and retrieve data easily, so in order to do this operation, we used the Database. We have used queries to pick and formulate the data in a specific structure from Database. This repo consists of a basic example of how to do that.


## Getting start

To get started with the code on this repo, you need to either *clone* or *download* this repo into your machine just as shown below;

```bash
git clone https://gitlab.com/mountblue/cohort-16-python/gopinath_v/dataproject-django-rest-framework
```

## Running the App

### Part 1: Create Database and virtualenv

### Move to project directory
```bash
$ cd dataproject-django-rest-framework
```

### Create Database
```bash
$ sudo -u postgres psql
```

```bash
postgres=# \i create_db.sql
```

```bash
postgres=# \q
```

### Install the virtualenv package
```bash
$ cd ..
$ pip install virtualenv
```
### Create the virtual environment
To create a virtual environment, you must specify a path. You may provide any name in the place of <mypython>:
```bash
$ virtualenv <mypython>
```
  
### Activate the virtual environment
```bash
$ source mypython/bin/activate
```

Now you can load the requirements.txt.
## Dependencies

Before running the application, you need to have some packages preinstalled. So I have provided all the required packages and their versions in requirements.txt file by running the below command you will be able to install all the packages.

```bash
$ cd dataproject-django-rest-framework
$ pip install -r requirements.txt
```

#### Part 1: Create and provide information to .env file.

To run this, you need to create and provide the environment values in .env file.

### Create .env file
create a .env file **inside studentapp folder**

```bash
$ cd api
$ touch .env
```
#### provide these information inside .env file.

```bash
SECURITY_KEY=GENERATED_ONE
```
##### NOTE: Do not provide space inbetween = and key,value inside .env file

#### open the terminal

#### SECRET_KEY generation

```bash
$ python3
>>> import secrets
>>> secrets.token_hex(16)
```
Provide **secret key** in .env file. 

#### for creating and accessing admin operations create superuser

```bash
cd ..
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
##### Note: provide your username and password in required place to create admin user.

#### Part 3: Running the application on server

```bash
$ python3 manage.py runserver

```

you can create the user by visiting register page ```http://127.0.0.1:8000/register/```

Now you can access the app on your local server but for performing operation in browser you need to provide the username and password of user created.

you can access the assignments api page through ```http://127.0.0.1:8000/viewset/assignments/```
#### part 4: Postman
## Install postman
```bash
sudo snap install postman
```
## Import collection ##

you can see the import option in your work space, click that and drop the file
**Assignment api.postman_collection.json** in that.

## Global variable ##

you need to set a global variable 

* VARIABLE - baseUrl
* INITIAL VALUE - http://localhost:8000
* CURRENT VALUE - http://localhost:8000

## API Authentication ##

To submit or view an order, you need to Authenticate.

You can login by both ways such as Basic Authentication and Token Authentication.

1. Basic Authentication:
In postman select basic auth in authorization and provide the provide the username 
and password of the registered user.  

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
}
```

you will get a token - youusertoken

Now select headers then, create a key called "Authorization" and a value 
called "Token yourusertoken"

## Run collection ##
Now you will be able to run the collection for testing.

### Deactivate the virtual environment
if you have followed step1, use this command to get out of virtualenv
```bash
$ deactivate

```
### Delete Database
```bash
$ sudo -u postgres psql
```

```bash
postgres=# \i delete_db.sql
```

```bash
postgres=# \q
```
