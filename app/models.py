from app import db

class Pribadi(db.Model):
    nrp = db.Column(db.Integer, primary_key=True, unique=True)
    ktp = db.Column(db.Integer, unique=True)
    kk = db.Column(db.Integer, unique=True)
    stnk = db.Column(db.Integer, unique=True)
    nama = db.Column(db.String(100))
    alamat = db.Column(db.Text)
    nomorHP = db.Column(db.Integer)

class Polsek(db.Model):
    kodePolsek = db.Column(db.Integer, primary_key=True, unique=True)
    namaPolsek = db.Column(db.String(100))
    alamatKantor = db.Column(db.String(100))

class Medcen(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    alamatKantor = db.Column(db.Text)

class DataLapor(db.Model):
    nama = db.Column(db.String(100), primary_key=True)
    kejadian = db.Column(db.Text)
    nomorHP = db.Column(db.Integer)
    lembagaBerwenang = db.Column(db.String(50))

class NomorLayanan(db.Model):
    kodePolsek = db.Column(db.Integer, primary_key=True)
    NomorLayananPolsek = db.Column(db.Integer)
    NomorLayananMedcen = db.Column(db.Integer)
    NomorDaruratPolsek = db.Column(db.Integer)

class WebsiteResmi(db.Model):
    kodePolsek = db.Column(db.Integer, primary_key=True)
    WebsiteResmiPolsek = db.Column(db.String(12))
    WebsiteResmiMedcen = db.Column(db.String(12))

class ProsedurLapor(db.Model):
    kodePolsek = db.Column(db.Integer, primary_key=True)    
    ProsedurLaporPolsek = db.Column(db.String(12))
    ProsedurLaporMedcen = db.Column(db.String(12))