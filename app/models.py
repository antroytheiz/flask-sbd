from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.Text, nullable=False)
    # posts = db.relationship('Post', backref='author', lazy=True)

class Pribadi(db.Model):
    nrp = db.Column(db.Integer, primary_key=True, unique=True)
    ktp = db.Column(db.Integer, unique=True)
    kk = db.Column(db.Integer, unique=True)
    stnk = db.Column(db.Integer, unique=True)
    nama = db.Column(db.String(100))
    alamat = db.Column(db.Text)
    nomorHP = db.Column(db.Integer)

class Polsek(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kodePolsek = db.Column(db.Integer, unique=False)
    namaPolsek = db.Column(db.String(100))
    alamatKantor = db.Column(db.String(100))

class Medcen(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    alamatKantor = db.Column(db.Text)

class DataLapor(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nama = db.Column(db.String(100))
    kejadian = db.Column(db.Text)
    nomorHP = db.Column(db.Integer)
    lembagaBerwenang = db.Column(db.String(50))

class NomorLayananPolsek(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kodePolsek = db.Column(db.Integer, unique=False)
    NomorLayananPolsek = db.Column(db.Integer, nullable=True)
    NomorDaruratPolsek = db.Column(db.Integer, nullable=True)

class NomorLayananMedcen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kodePolsek = db.Column(db.Integer, unique=False)
    NomorLayananMedcen = db.Column(db.Integer, nullable=True)

class WebsiteResmiPolsek(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kodePolsek = db.Column(db.Integer, unique=False)
    WebsiteResmiPolsek = db.Column(db.String(12), nullable=True)

class WebsiteResmiMedcen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kodePolsek = db.Column(db.Integer, unique=False)
    WebsiteResmiMedcen = db.Column(db.String(12), nullable=True)    

class ProsedurLaporPolsek(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    kodePolsek = db.Column(db.Integer, unique=False)
    ProsedurLaporPolsek = db.Column(db.Text, nullable=True)

class ProsedurLaporMedcen(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    kodePolsek = db.Column(db.Integer, unique=False)
    ProsedurLaporMedcen = db.Column(db.Text, nullable=True)