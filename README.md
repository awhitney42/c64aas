# c64aas
Commodore 64 as a Service

- GET /api/program - LIST the program.
- POST /api/program - Create a NEW program.
- _PUT /api/program - Append to the program. (NOT YET IMPLEMENTED)_
- GET /api/program/<line number> - LIST the specified line number from the program.
- _PUT /api/program/<line number> - Update the line number in the program. (NOT YET IMPLEMENTED)_
- GET /api/run - RUN the program and return the output.


## REQUIREMENTS

This requires the cbmbasic program.

- https://github.com/mist64/cbmbasic

## HOW TO RUN

Activate a Python virtual enviroment.
```console
 $ python -m venv venv
 $ source venv/bin/activate
 (venv) $
```

Install Flask and Connexion.
```console
 (venv) $ python -m pip install Flask==2.2.2
 (venv) $ python -m pip install "connexion[swagger-ui]==2.14.1"
```
Run the App.
```console
 (venv) $ python app.py
```

Navigate to http://localhost:8000 to learn more.

Also check out the c64aas.postman_collection.json Postman collection for more info.
