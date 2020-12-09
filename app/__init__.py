from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'dawfvdfsge'

# Initialisation App
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'theis'
app.config['MYSQL_PASSWORD'] = 'salupa'
app.config['MYSQL_DB'] = 'proyek2'


mysql = MySQL(app)

from app import routes