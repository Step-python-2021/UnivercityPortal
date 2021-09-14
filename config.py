from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd917274a73d200ab842c70309624f5ba'
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'university_db'

mysql = MySQL()
mysql.init_app(app)
