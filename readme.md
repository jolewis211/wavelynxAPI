# Instructions for use

#### Install dependencies via your terminal with "```pipenv sync```"

####  To build the expected database, inside of your postgreSQL terminal run:
```CREATE USER wl_user WITH PASSWORD 'password';```

```CREATE DATABASE tokendb WITH OWNER wl_user;```

#### At the root level create a ```.flaskenv``` copy in the following information 
```FLASK_APP=app/app.py```

```FLASK_ENV=development```

```FLASK_RUN_PORT=8080```

```SECRET_KEY=rhW0ze@@BX#%```

```DATABASE_URL=postgresql://wl_user:password@localhost/tokendb```

#### In the terminal at the root level run
```flask db init```

```flask db migrate```

```flask db upgrade```


#### Now that your dependencies are installed and the expected database is built start the application with ```flask run```


#### This application can handle GET requests at ```localhost:8080/token```.  It will automatically generate and store valid tokens in the database.


#### This application can also handle POST requests at ```localhost:8080/verify```.  Requests must be valid JSON request with ```Content-Type: application/JSON``` headers.  This API expects this format: ```{"token": "1'=Y..."}```
