1. create virtual environment by running the following command in a bash shell, in your project folder

    python -m venv venv

2. go to command palette in vs code and select:

    'python: select interpreter'  -> select the one that says '(venv:venv)

3. if you dont see '(venv)' in terminal (if virtual environment did not start automatically):
    1. kill terminal (trash can)
    2. enter: . venv/scripts/activate

    ---- to deactivate virtual environement ---
    type in the following to the bash terminal : deactivate

4. using 'requirements.txt' in the project folder (this is where all of the packages needed for the project are)
    enter the following into the terminal : python -m pip install -r requirements.txt


5. create app file in python: import flask...

6. to run flask : make sure terminal is set to bash
    if you want to run flask in a development environment:
    export FLASK_ENV=development

    export FLASK_APP=ez_stocks ... in this case, ez_stocks is the name of the app
    flask run

7. crate database
    docker exec -i pg_container psql -c 'CREATE DATABASE stocks' (stocks in the name of the db)


to check db contents in terminal:
    docker exec -it pg_container psql
    \c stocks
    \dt

    