from flask import Flask
# from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'dawfvdfsge'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sbd_proyek.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://theis:salupa@localhost/sbdproyek'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# # Initialisation App
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'theis'
# app.config['MYSQL_PASSWORD'] = 'salupa'
# app.config['MYSQL_DB'] = 'sbdproyek'
# mysql = MySQL(app)

from app import routes