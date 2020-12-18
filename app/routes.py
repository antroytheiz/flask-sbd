from app import app, db
from flask import render_template, request, redirect, url_for, flash
from .models import (Pribadi, Polsek, Medcen, DataLapor, 
                    NomorLayananPolsek, NomorLayananMedcen, WebsiteResmiPolsek, WebsiteResmiMedcen, 
                    ProsedurLaporPolsek, ProsedurLaporMedcen, User)
from flask_login import login_user, current_user, logout_user, login_required
from .forms import LoginForm



@app.route('/dashboard')
@login_required
def home():    
    return render_template('index.html', title='Dashboard', menu='dashboard', 
    data=Pribadi.query.all(), data2=Polsek.query.all(), data3=Medcen.query.all(), data4a=ProsedurLaporPolsek.query.all(), 
    data4b=ProsedurLaporMedcen.query.all(), data5a=NomorLayananPolsek.query.all(), data5b=NomorLayananMedcen.query.all(), 
    data6a=WebsiteResmiPolsek.query.all(),data6b=WebsiteResmiMedcen.query.all(), data7=DataLapor.query.all())

@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        password = User.query.filter_by(password=form.password.data).first()
        if user and password:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
            # return redirect(url_for('home'))
    return render_template ('login.html', form=form, title='Login')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/pribadi/')
@login_required
def pribadi():
    return render_template('pribadi/pribadi.html', title='Pribadi', submenu='dataPribadi', link1='Data Pribadi' ,data=Pribadi.query.all())

@app.route('/pribadi/tambah/', methods=['GET','POST'])
@login_required
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
@login_required
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
@login_required
def pribadiDel(nrp):
    data = Pribadi.query.filter_by(nrp=nrp).first()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('pribadi'))
# Akhir Pribadi


# Awal DataLapor
@app.route('/data_lapor/')
@login_required
def lapor():
    return render_template('lapor/lapor.html', title='Data Lapor', submenu='data Lapor', link1='Data Lapor' ,data=DataLapor.query.all())

@app.route('/data_lapor/tambah/', methods=['GET','POST'])
@login_required
def laporAdd():
    if request.method == 'POST':
        nama = request.form['nama']
        kejadian = request.form['kejadian']
        nomorHP = request.form['nophone']
        lembaga = request.form['lembaga']
        data = DataLapor(nama=nama, kejadian=kejadian, nomorHP=nomorHP, lembagaBerwenang=lembaga)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('lapor'))
    else:
        return render_template('lapor/laporAdd.html', title='Data Lapor', submenu='data Lapor', link1='Data Lapor', link2='Tambah Data Lapor', link3='lapor/', data2=Pribadi.query.all())

@app.route('/data_lapor/<id>/ubah/', methods=['GET','POST'])
@login_required
def laporEdit(id):
    data = DataLapor.query.filter_by(id=id).first()
    if request.method == 'POST':
        data.nama = request.form['nama']
        data.kejadian = request.form['kejadian']
        data.nomorHP = request.form['nophone']
        data.lembagaBerwenang = request.form['lembaga']
        db.session.commit()
        return redirect(url_for('lapor'))
    else:
        return render_template('lapor/laporAdd.html', title='Ubah Lapor', submenu='data Lapor' ,link1='Data Lapor', link2='Ubah Data Lapor', link3='lapor/', data=data)

@app.route('/data_lapor/<id>/hapus/', methods=['GET','POST'])
@login_required
def laporDel(id):
    data = DataLapor.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('lapor'))

# Akhir DataLapor


# Awal Polsek

@app.route('/polsek/')
@login_required
def polsek():
    return render_template('polsek/polsek.html', title='Polsek', submenu='dataPolsek', link1='Data Polsek' ,data=Polsek.query.all())

@app.route('/polsek/tambah/', methods=['GET','POST'])
@login_required
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
@login_required
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
@login_required
def polsekDel(kodePolsek):
    data = Polsek.query.filter_by(kodePolsek=kodePolsek).first()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('polsek'))

# Akhir Polsek


# Awal Medcen

@app.route('/medcen/')
@login_required
def medcen():
    return render_template('medcen/medcen.html', title='Medcen', submenu='dataMedcen', link1='Data Medcen' ,data=Medcen.query.all())

@app.route('/medcen/tambah/', methods=['GET','POST'])
@login_required
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
@login_required
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
@login_required
def delMedcen(id):
    data = Medcen.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('medcen'))

# Akhir Medcen




# Awal Prosedur

@app.route('/prosedur/')
@login_required
def prosedur():
    return render_template('prosedur/prosedur.html', title='Prosedur', submenu='dataProsedur', link1='Data Prosedur' ,data=ProsedurLaporPolsek.query.all(), data2=ProsedurLaporMedcen.query.all())

@app.route('/prosedur/tambah/', methods=['GET','POST'])
@login_required
def prosedurAdd():
    if request.method == 'POST':
        kodePolsek = request.form['kodePolsek']
        if current_user.username == 'polsek':
            laporPolsek = request.files['laporPolsek']
            data = ProsedurLaporPolsek(kodePolsek=kodePolsek, ProsedurLaporPolsek=laporPolsek.filename)
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('prosedur'))
        if current_user.username == 'medcen':            
            laporMedcen = request.files['laporMedcen']
            data2 = ProsedurLaporMedcen(kodePolsek=kodePolsek, ProsedurLaporMedcen=laporMedcen.filename)
            db.session.add(data2)
            db.session.commit()
            return redirect(url_for('prosedur'))
    else:
        return render_template('prosedur/prosedurAdd.html', title='Tambah Prosedur', submenu='dataProsedur' ,link1='Data Prosedur', link2='Tambah Data Prosedur', link3='polsek/', dataPolsek=Polsek.query.all())

# @app.route('/prosedur/<id>/ubah/', methods=['GET','POST'])
# @login_required
# def prosedurEdit(id):
#     if current_user.username == 'polsek':
#         data = ProsedurLaporPolsek.query.filter_by(id=id).first()
#     if current_user.username == 'medcen':
#         data2 = ProsedurLaporMedcen.query.filter_by(id=id).first()
#     if request.method == 'POST':
#         if current_user.username == 'polsek':
#             data.kodePolsek = request.form['kodePolsek']
#             data.ProsedurLaporPolsek = request.files['laporPolsek']
#             db.session.commit()
#             return redirect(url_for('prosedur'))
#         if current_user.username == 'medcen':
#             data2.kodePolsek = request.form['kodePolsek']
#             data2.ProsedurLaporMedcen = request.files['laporMedcen']
#             db.session.commit()
#             return redirect(url_for('prosedur'))
#     else:
#         return render_template('prosedur/prosedurAdd.html', title='Ubah Prosedur', submenu='dataProsedur' ,link1='Data Prosedur', link2='Ubah Data Prosedur', link3='prosedur/', data=data, dataPolsek=Polsek.query.all())

@app.route('/prosedur/<id>/hapus/', methods=['GET','POST'])
@login_required
def prosedurDel(id):
    if current_user.username == 'polsek':
        data = ProsedurLaporPolsek.query.filter_by(id=id).first()
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for('prosedur'))
    if current_user.username == 'medcen':
        data2 = ProsedurLaporMedcen.query.filter_by(id=id).first()
        db.session.delete(data2)
        db.session.commit()
        return redirect(url_for('prosedur'))

# # Akhir Polsek


# Awal NomorLayanan

@app.route('/nomor_layanan/')
@login_required
def layanan():
    return render_template('layanan/layanan.html', title='Nomor Layanan', submenu='dataNomor Layanan', link1='Data Nomor Layanan' ,data=NomorLayananPolsek.query.all(), data2=NomorLayananMedcen.query.all())

@app.route('/nomor_layanan/tambah/', methods=['GET','POST'])
@login_required
def layananAdd():
    if request.method == 'POST':
        kodePolsek = request.form['kodePolsek']
        if current_user.username == 'polsek':
            layananPolsek = request.form['layananPolsek']
            daruratPolsek = request.form['daruratPolsek']
            data = NomorLayananPolsek(kodePolsek=kodePolsek, NomorLayananPolsek=layananPolsek, NomorDaruratPolsek=daruratPolsek)
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('layanan'))
        if current_user.username == 'medcen':
            layananMedcen = request.form['layananMedcen']
            data2 = NomorLayananMedcen(kodePolsek=kodePolsek, NomorLayananMedcen=layananMedcen)
            db.session.add(data2)
            db.session.commit()
            return redirect(url_for('layanan'))
    else:
        return render_template('layanan/layananAdd.html', title='Tambah Nomor Layanan', submenu='dataNomor Layanan' ,link1='Data Nomor Layanan', link2='Tambah Data Nomor Layanan', link3='nomor_layanan/', dataPolsek=Polsek.query.all())

@app.route('/nomor_layanan/<id>/ubah/', methods=['GET','POST'])
@login_required
def layananEdit(id):
    data = NomorLayananPolsek.query.filter_by(id=id).first()
    data2 = NomorLayananMedcen.query.filter_by(id=id).first()
    if request.method == 'POST':
        if current_user.username == 'polsek':
            data.kodePolsek = request.form['kodePolsek']
            data.NomorLayananPolsek = request.form['layananPolsek']
            data.NomorDaruratPolsek = request.form['daruratPolsek']
            db.session.commit()
            return redirect(url_for('layanan'))
        if current_user.username == 'medcen':
            data2.kodePolsek = request.form['kodePolsek']
            data2.NomorLayananMedcen = request.form['layananMedcen']
            db.session.commit()
            return redirect(url_for('layanan'))
    else:
        return render_template('layanan/layananAdd.html', title='Ubah Nomor Layanan', submenu='dataNomor Layanan' ,link1='Data Nomor Layanan', link2='Ubah Data Nomor Layanan', link3='nomor_layanan/',data2=data2, data=data,  dataPolsek=Polsek.query.all())

@app.route('/nomor_layanan/<id>/hapus/', methods=['GET','POST'])
@login_required
def layananDel(id):
    if current_user.username == 'polsek':
        data = NomorLayananPolsek.query.filter_by(id=id).first()
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for('layanan'))
    elif current_user.username == 'medcen':
        data2 = NomorLayananMedcen.query.filter_by(id=id).first()
        db.session.delete(data2)
        db.session.commit()
        return redirect(url_for('layanan'))        

# Akhir NomorLayanan


# Awal WebsiteResmi

@app.route('/website_resmi/')
@login_required
def webresmi():
    return render_template('webresmi/webresmi.html', title='Website Resmi', submenu='dataWebsite Resmi', link1='Data Website Resmi' ,data=WebsiteResmiPolsek.query.all(), data2=WebsiteResmiMedcen.query.all())

@app.route('/website_resmi/tambah/', methods=['GET','POST'])
@login_required
def webresmiAdd():
    if request.method == 'POST':
        kodePolsek = request.form['kodePolsek']
        if current_user.username == 'polsek':
            webPolsek = request.form['webPolsek']
            data = WebsiteResmiPolsek(kodePolsek=kodePolsek, WebsiteResmiPolsek=webPolsek)
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('webresmi'))
        if current_user.username == 'medcen':
            webMedcen = request.form['webMedcen']
            data2 = WebsiteResmiMedcen(kodePolsek=kodePolsek, WebsiteResmiMedcen=webMedcen)
            db.session.add(data2)
            db.session.commit()
            return redirect(url_for('webresmi'))
    else:
        return render_template('webresmi/webresmiAdd.html', title='Tambah Website Resmi', submenu='dataWebsite Resmi' ,link1='Data Website Resmi', link2='Tambah Data Website Resmi', link3='website_resmi/', dataPolsek=Polsek.query.all())

@app.route('/website_resmi/<id>/ubah/', methods=['GET','POST'])
@login_required
def webresmiEdit(id):
    data = WebsiteResmiPolsek.query.filter_by(id=id).first()
    data2 = WebsiteResmiMedcen.query.filter_by(id=id).first()
    if request.method == 'POST':
        if current_user.username == 'polsek':
            data.kodePolsek = request.form['kodePolsek']
            data.WebsiteResmiPolsek = request.form['webPolsek']
            db.session.commit()
            return redirect(url_for('webresmi'))
        if current_user.username == 'medcen':
            data2.kodePolsek = request.form['kodePolsek']
            data2.WebsiteResmiMedcen = request.form['webMedcen']
            db.session.commit()
            return redirect(url_for('webresmi'))
    else:
        return render_template('webresmi/webresmiAdd.html', title='Ubah Website Resmi', submenu='dataWebsite Resmi' ,link1='Data Website Resmi', link2='Ubah Data Website Resmi', link3='website_resmi/',data2=data2, data=data,  dataPolsek=Polsek.query.all())

@app.route('/website_resmi/<id>/hapus/', methods=['GET','POST'])
@login_required
def webresmiDel(id):
    if current_user.username == 'polsek':
        data = WebsiteResmiPolsek.query.filter_by(id=id).first()
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for('webresmi'))
    elif current_user.username == 'medcen':
        data2 = WebsiteResmiMedcen.query.filter_by(id=id).first()
        db.session.delete(data2)
        db.session.commit()
        return redirect(url_for('webresmi'))    

# Akhir WebsiteResmi





