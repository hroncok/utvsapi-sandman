import sandman2
from sqlalchemy.engine.url import URL

from utvsapi import models

url = URL('mysql', query={'read_default_file': './mysql.cnf'})
app = sandman2.get_app(url, user_models=models.all(), read_only=True)

if __name__ == '__main__':
    app.run(debug=True)
