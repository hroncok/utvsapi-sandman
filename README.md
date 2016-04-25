utvsapi-sandman
===============

A REST-like read-only API for [ÚTVS ČVUT](https://rozvoj.fit.cvut.cz/Main/rozvrhy-utvs-db)
implemented in [sandman2](https://github.com/jeffknupp/sandman2).

To use this, create file named `mysql.cnf` with your MySQL credentials, see an example here:

    [client]
    host = localhost
    user = username
    database = dbname
    password = insecurepassword

This has been developed and run on Python 3 only, legacy Python might not work.

Install `sandman2` and `mysqlclient` (you'll need mysql devel package for that). You might do it with virtualenv:

    pyvenv venv
    . venv/bin/activate
    pip install sandman2 mysqlclient

Start the service in debug mode:

    PYTHONPATH=. python3 utvsapi/main.py

Or run with gunicorn:

    pip install gunicorn
    PYTHONPATH=. gunicorn utvsapi.main:app

License
-------

This software is licensed under the terms of the MIT license, see LICENSE for full text and copyright information.
