from app import app, db
from flask import render_template, request, redirect, url_for
from .models import (Pribadi, Polsek, Medcen, DataLapor, 
                    NomorLayanan, WebsiteResmi, ProsedurLapor)

@app.route('/')
@app.route('/dashboard')
def home():    
    return render_template('index.html', title='Dashboard', menu='dashboard', 
    data=Pribadi.query.all(), data2=Polsek.query.all())

@app.route('/pribadi/')
def pribadi():
    return render_template('pribadi/pribadi.html', title='Pribadi', submenu='dataPribadi', link1='Data Pribadi' ,data=Pribadi.query.all())

@app.route('/pribadi/tambah/', methods=['GET','POST'])
def pribadiAdd():
    if request.method == 'POST':
        nrp = request.form['nrp']
        ktp = request.form['ktp']
        kk = request.form['kk']
        stnk = request.form['stnk']
        nama = request.form['nama']
        alamat = request.form['alamat']
        nophone = request.form['nophone']
        data = Pribadi(nrp=nrp, ktp=ktp, kk=kk, stnk=stnk, nama=nama, alamat=alamat, nomorHP=nophone)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('pribadi'))
    else:
        return render_template('pribadi/pribadiAdd.html', title='Tambah Pribadi', submenu='dataPribadi' ,link1='Data Pribadi', link2='Tambah Data Pribadi', link3='pribadi/')

@app.route('/pribadi/<nrp>/ubah/', methods=['GET','POST'])
def pribadiEdit(nrp):
    data = Pribadi.query.filter_by(nrp=nrp).first()
    if request.method == 'POST':
        data.nrp = request.form['nrp']
        data.ktp = request.form['ktp']
        data.kk = request.form['kk']
        data.stnk = request.form['stnk']
        data.nama = request.form['nama']
        data.alamat = request.form['alamat']
        data.nomorHP = request.form['nophone']
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('pribadi'))
    else:
        return render_template('pribadi/pribadiAdd.html', title='Ubah Pribadi', submenu='dataPribadi' ,link1='Data Pribadi', link2='Ubah Data Pribadi', link3='pribadi/', data=data)

@app.route('/pribadi/<nrp>/hapus/', methods=['GET','POST'])
def pribadiDel(nrp):
    data = Pribadi.query.filter_by(nrp=nrp).first()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('pribadi'))

# Akhir Pribadi


# Awal Polsek

@app.route('/polsek/')
def polsek():
    return render_template('polsek/polsek.html', title='Polsek', submenu='dataPolsek', link1='Data Polsek' ,data=Polsek.query.all())

@app.route('/polsek/tambah/', methods=['GET','POST'])
def polsekAdd():
    if request.method == 'POST':
        kodePolsek = request.form['kdPolsek']
        namaPolsek = request.form['namaPolsek']
        alamatPolsek = request.form['alamat']
        data = Polsek(kodePolsek=kodePolsek, namaPolsek=namaPolsek, alamatKantor=alamatPolsek)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('polsek'))
    else:
        return render_template('polsek/polsekAdd.html', title='Tambah Polsek', submenu='dataPolsek' ,link1='Data Polsek', link2='Tambah Data polsek', link3='polsek/')

@app.route('/polsek/<kodePolsek>/ubah/', methods=['GET','POST'])
def polsekEdit(kodePolsek):
    data = Polsek.query.filter_by(kodePolsek=kodePolsek).first()
    if request.method == 'POST':
        data.kodePolsek = request.form['kdPolsek']
        data.namaPolsek = request.form['namaPolsek']
        data.alamatKantor = request.form['alamat']
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('polsek'))
    else:
        return render_template('polsek/polsekAdd.html', title='Ubah Polsek', submenu='dataPolsek' ,link1='Data Polsek', link2='Ubah Data Polsek', link3='polsek/', data=data)

@app.route('/polsek/<kodePolsek>/hapus/', methods=['GET','POST'])
def polsekDel(kodePolsek):
    data = Polsek.query.filter_by(kodePolsek=kodePolsek).first()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('polsek'))

# Akhir Polsek


# Awal Medcen

@app.route('/medcen/')
def medcen():
    return render_template('medcen/medcen.html', title='Medcen', submenu='dataMedcen', link1='Data Medcen' ,data=Medcen.query.all())

@app.route('/medcen/tambah/', methods=['GET','POST'])
def medcenAdd():
    if request.method == 'POST':
        alamatKantor = request.form['alamatKantor']
        data = Medcen(alamatKantor=alamatKantor)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('medcen'))
    else:
        return render_template('medcen/medcenAdd.html', title='Tambah Medcen', submenu='dataMedcen' ,link1='Data Medcen', link2='Tambah Data Medcen', link3='medcen/')

@app.route('/medcen/<id>/ubah/', methods=['GET','POST'])
def medcenEdit(id):
    data = Medcen.query.filter_by(id=id).first()
    if request.method == 'POST':
        data.alamatKantor = request.form['alamatKantor']
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('medcen'))
    else:
        return render_template('medcen/medcenAdd.html', title='Ubah Medcen', submenu='dataMedcen' ,link1='Data Medcen', link2='Ubah Data Medcen', link3='medcen/', data=data)

@app.route('/medcen/<id>/hapus/', methods=['GET','POST'])
def delMedcen(id):
    data = Medcen.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('medcen'))

# Akhir Medcen


# Awal Polsek

# @app.route('/polsek/')
# def polsek():
#     return render_template('polsek/polsek.html', title='Polsek', submenu='dataPolsek', link1='Data Polsek' ,data=Polsek.query.all())

# @app.route('/polsek/tambah/', methods=['GET','POST'])
# def polsekAdd():
#     if request.method == 'POST':
#         kodePolsek = request.form['kdPolsek']
#         namaPolsek = request.form['namaPolsek']
#         alamatPolsek = request.form['alamat']
#         data = Polsek(kodePolsek=kodePolsek, namaPolsek=namaPolsek, alamatKantor=alamatPolsek)
#         db.session.add(data)
#         db.session.commit()
#         return redirect(url_for('polsek'))
#     else:
#         return render_template('polsek/polsekAdd.html', title='Tambah Polsek', submenu='dataPolsek' ,link1='Data Polsek', link2='Tambah Data polsek', link3='polsek/')

# @app.route('/polsek/<kodePolsek>/ubah/', methods=['GET','POST'])
# def polsekEdit(kodePolsek):
#     data = Polsek.query.filter_by(kodePolsek=kodePolsek).first()
#     if request.method == 'POST':
#         data.kodePolsek = request.form['kdPolsek']
#         data.namaPolsek = request.form['namaPolsek']
#         data.alamatKantor = request.form['alamat']
#         db.session.add(data)
#         db.session.commit()
#         return redirect(url_for('polsek'))
#     else:
#         return render_template('polsek/polsekAdd.html', title='Ubah Polsek', submenu='dataPolsek' ,link1='Data Polsek', link2='Ubah Data Polsek', link3='polsek/', data=data)

# @app.route('/polsek/<kodePolsek>/hapus/', methods=['GET','POST'])
# def polsekDel(kodePolsek):
#     data = Polsek.query.filter_by(kodePolsek=kodePolsek).first()
#     db.session.delete(data)
#     db.session.commit()
#     return redirect(url_for('polsek'))

# # Akhir Polsek


# # Awal Polsek

# @app.route('/polsek/')
# def polsek():
#     return render_template('polsek/polsek.html', title='Polsek', submenu='dataPolsek', link1='Data Polsek' ,data=Polsek.query.all())

# @app.route('/polsek/tambah/', methods=['GET','POST'])
# def polsekAdd():
#     if request.method == 'POST':
#         kodePolsek = request.form['kdPolsek']
#         namaPolsek = request.form['namaPolsek']
#         alamatPolsek = request.form['alamat']
#         data = Polsek(kodePolsek=kodePolsek, namaPolsek=namaPolsek, alamatKantor=alamatPolsek)
#         db.session.add(data)
#         db.session.commit()
#         return redirect(url_for('polsek'))
#     else:
#         return render_template('polsek/polsekAdd.html', title='Tambah Polsek', submenu='dataPolsek' ,link1='Data Polsek', link2='Tambah Data polsek', link3='polsek/')

# @app.route('/polsek/<kodePolsek>/ubah/', methods=['GET','POST'])
# def polsekEdit(kodePolsek):
#     data = Polsek.query.filter_by(kodePolsek=kodePolsek).first()
#     if request.method == 'POST':
#         data.kodePolsek = request.form['kdPolsek']
#         data.namaPolsek = request.form['namaPolsek']
#         data.alamatKantor = request.form['alamat']
#         db.session.add(data)
#         db.session.commit()
#         return redirect(url_for('polsek'))
#     else:
#         return render_template('polsek/polsekAdd.html', title='Ubah Polsek', submenu='dataPolsek' ,link1='Data Polsek', link2='Ubah Data Polsek', link3='polsek/', data=data)

# @app.route('/polsek/<kodePolsek>/hapus/', methods=['GET','POST'])
# def polsekDel(kodePolsek):
#     data = Polsek.query.filter_by(kodePolsek=kodePolsek).first()
#     db.session.delete(data)
#     db.session.commit()
#     return redirect(url_for('polsek'))

# # Akhir Polsek


# # Awal Polsek

# @app.route('/polsek/')
# def polsek():
#     return render_template('polsek/polsek.html', title='Polsek', submenu='dataPolsek', link1='Data Polsek' ,data=Polsek.query.all())

# @app.route('/polsek/tambah/', methods=['GET','POST'])
# def polsekAdd():
#     if request.method == 'POST':
#         kodePolsek = request.form['kdPolsek']
#         namaPolsek = request.form['namaPolsek']
#         alamatPolsek = request.form['alamat']
#         data = Polsek(kodePolsek=kodePolsek, namaPolsek=namaPolsek, alamatKantor=alamatPolsek)
#         db.session.add(data)
#         db.session.commit()
#         return redirect(url_for('polsek'))
#     else:
#         return render_template('polsek/polsekAdd.html', title='Tambah Polsek', submenu='dataPolsek' ,link1='Data Polsek', link2='Tambah Data polsek', link3='polsek/')

# @app.route('/polsek/<kodePolsek>/ubah/', methods=['GET','POST'])
# def polsekEdit(kodePolsek):
#     data = Polsek.query.filter_by(kodePolsek=kodePolsek).first()
#     if request.method == 'POST':
#         data.kodePolsek = request.form['kdPolsek']
#         data.namaPolsek = request.form['namaPolsek']
#         data.alamatKantor = request.form['alamat']
#         db.session.add(data)
#         db.session.commit()
#         return redirect(url_for('polsek'))
#     else:
#         return render_template('polsek/polsekAdd.html', title='Ubah Polsek', submenu='dataPolsek' ,link1='Data Polsek', link2='Ubah Data Polsek', link3='polsek/', data=data)

# @app.route('/polsek/<kodePolsek>/hapus/', methods=['GET','POST'])
# def polsekDel(kodePolsek):
#     data = Polsek.query.filter_by(kodePolsek=kodePolsek).first()
#     db.session.delete(data)
#     db.session.commit()
#     return redirect(url_for('polsek'))

# # Akhir Polsek


# # Awal Polsek

# @app.route('/polsek/')
# def polsek():
#     return render_template('polsek/polsek.html', title='Polsek', submenu='dataPolsek', link1='Data Polsek' ,data=Polsek.query.all())

# @app.route('/polsek/tambah/', methods=['GET','POST'])
# def polsekAdd():
#     if request.method == 'POST':
#         kodePolsek = request.form['kdPolsek']
#         namaPolsek = request.form['namaPolsek']
#         alamatPolsek = request.form['alamat']
#         data = Polsek(kodePolsek=kodePolsek, namaPolsek=namaPolsek, alamatKantor=alamatPolsek)
#         db.session.add(data)
#         db.session.commit()
#         return redirect(url_for('polsek'))
#     else:
#         return render_template('polsek/polsekAdd.html', title='Tambah Polsek', submenu='dataPolsek' ,link1='Data Polsek', link2='Tambah Data polsek', link3='polsek/')

# @app.route('/polsek/<kodePolsek>/ubah/', methods=['GET','POST'])
# def polsekEdit(kodePolsek):
#     data = Polsek.query.filter_by(kodePolsek=kodePolsek).first()
#     if request.method == 'POST':
#         data.kodePolsek = request.form['kdPolsek']
#         data.namaPolsek = request.form['namaPolsek']
#         data.alamatKantor = request.form['alamat']
#         db.session.add(data)
#         db.session.commit()
#         return redirect(url_for('polsek'))
#     else:
#         return render_template('polsek/polsekAdd.html', title='Ubah Polsek', submenu='dataPolsek' ,link1='Data Polsek', link2='Ubah Data Polsek', link3='polsek/', data=data)

# @app.route('/polsek/<kodePolsek>/hapus/', methods=['GET','POST'])
# def polsekDel(kodePolsek):
#     data = Polsek.query.filter_by(kodePolsek=kodePolsek).first()
#     db.session.delete(data)
#     db.session.commit()
#     return redirect(url_for('polsek'))

# # Akhir Polsek