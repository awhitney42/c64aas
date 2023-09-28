# c64aas
Commodore 64 as a Service

## Current API
- GET /api/program - LIST the program.
- POST /api/program - Create a NEW program.
- GET /api/program/&lt;line number&gt; - LIST the specified line number in the program.
- GET /api/run - RUN the program and return the output.

## Coming Soon

- _PUT /api/program - Append to the program. (NOT YET IMPLEMENTED)_
- _PUT /api/program/&lt;line number&gt; - Update the line number in the program. (NOT YET IMPLEMENTED)_


## REQUIREMENTS

This requires the cbmbasic program to be in the environment path.

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

