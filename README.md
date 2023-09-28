# c64aas
Commodore 64 as a Service

## REQUIREMENTS

This requires the cbmbasic program.

- https://github.com/mist64/cbmbasic

## HOW TO RUN

Activate a Python virtual enviroment.

 $ python -m venv venv
 $ source venv/bin/activate
 (venv) $

Install Flask and Connexion.

 (venv) $ python -m pip install Flask==2.2.2
 (venv) $ python -m pip install "connexion[swagger-ui]==2.14.1"

Run the App.

 (venv) $ python app.py

Navigate to http://localhost:8000 to learn more.

Also check out the c64aas.postman_collection.json Postman collection for more info.
