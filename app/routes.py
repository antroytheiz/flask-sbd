from app import app, mysql
from flask import render_template, request, redirect, url_for
import os

@app.route('/')
@app.route('/dashboard')
def home():
    # Pertama
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM Pribadi;
    ''')
    data = []
    for nrp,ktp,kk,stnk,nama,alamat,nophone,kdPolsek in cur.fetchall():
        data.append((nrp,ktp,kk,stnk,nama,alamat,nophone,kdPolsek))
    cur.close()
    

    # Kedua
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM Polsek;
    ''')
    data2 = []
    for kd,alamatPol,namaPol in cur.fetchall():
        data2.append((kd,alamatPol,namaPol))
    cur.close()

    # Ketiga
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM MedcenITS;
    ''')
    data3 = []
    for nrp,alamatKantor in cur.fetchall():
        data3.append((nrp,alamatKantor))
    cur.close()

    # KeEmpat
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM ProsedurLapor;
    ''')
    data4 = []
    for kd,pLp,pLm in cur.fetchall():
        data4.append((kd,pLp,pLm))
    cur.close()

    # Kelima
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM NomorLayanan;
    ''')
    data5= []
    for kd,nLp,nLm,nDp in cur.fetchall():
        data5.append((kd,nLp,nLm,nDp))
    cur.close()

    # Keenam
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM WebsiteResmi;
    ''')
    data6 = []
    for kd,WebsiteResmiPol,WebsiteResmiMed in cur.fetchall():
        data6.append((kd,WebsiteResmiPol,WebsiteResmiMed))
    cur.close()

    # Ketujuh
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM DataLapor;
    ''')
    data7 = []
    for nama,kejadian,nophone,lBer in cur.fetchall():
        data7.append((nama,kejadian,nophone,lBer))
    cur.close()

    return render_template('index.html', title='Dashboard', menu='dashboard', data=data, data2=data2, data3=data3, data4=data4, data5=data5, data6=data6, data7=data7)

@app.route('/pribadi/')
def pribadi():
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM Pribadi;
    ''')
    data = []
    for nrp,ktp,kk,stnk,nama,alamat,nophone,kdPolsek in cur.fetchall():
        data.append((nrp,ktp,kk,stnk,nama,alamat,nophone,kdPolsek))
    cur.close()
    return render_template('pribadi/pribadi.html', title='Pribadi', submenu='dataPribadi', link1='Data Pribadi' ,data=data)

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
        kodePolsek = request.form['kodePolsek']
        data = (nrp, ktp, kk, stnk, nama, alamat, nophone, kodePolsek)
        cur = mysql.connection.cursor()
        cur.execute('''
            INSERT INTO Pribadi VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')
        ''' % data)
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('pribadi'))
    else:
        return render_template('pribadi/pribadiAdd.html', title='Tambah Pribadi', submenu='dataPribadi' ,link1='Data Pribadi', link2='Tambah Data Pribadi', link3='pribadi/')

@app.route('/pribadi/<nrp>/ubah/', methods=['GET','POST'])
def pribadiEdit(nrp):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Pribadi WHERE nrp='%s' " % nrp)
    data = cur.fetchone()
    if request.method == 'POST':
        nrp = request.form['nrp']
        ktp = request.form['ktp']
        kk = request.form['kk']
        stnk = request.form['stnk']
        nama = request.form['nama']
        alamat = request.form['alamat']
        nophone = request.form['nophone']
        cur.execute('''
            UPDATE Pribadi SET ktp='%s', kk='%s', stnk='%s',
            nama='%s', alamat='%s', nomorHP='%s' WHERE nrp='%s'
        ''' % ( ktp, kk, stnk, nama, alamat, nophone, nrp))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('pribadi'))
    else:
        cur.close()
        print(data)
        return render_template('pribadi/pribadiAdd.html', title='Ubah Pribadi', submenu='dataPribadi' ,link1='Data Pribadi', link2='Ubah Data Pribadi', link3='pribadi/', data=data)

@app.route('/pribadi/<nrp>/hapus/', methods=['GET','POST'])
def pribadiDel(nrp):
    cur = mysql.connection.cursor()
    cur.execute('''
        DELETE FROM Pribadi WHERE nrp='%s'
    ''' % nrp)
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('pribadi'))

# Akhir Pribadi


# Awal Polsek
@app.route('/polsek/')
def polsek():
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM Polsek;
    ''')
    data = []
    for kd,alamatPol,namaPol in cur.fetchall():
        data.append((kd,alamatPol,namaPol))
    cur.close()
    return render_template('polsek/polsek.html', title='Polsek', submenu='dataPolsek', link1='Data Polsek' ,data=data)


@app.route('/polsek/tambah/', methods=['GET','POST'])
def polsekAdd():
    if request.method == 'POST':
        kdPolsek = request.form['kdPolsek']
        namaPolsek = request.form['namaPolsek']
        alamat = request.form['alamat']
        data = (kdPolsek, namaPolsek, alamat)
        cur = mysql.connection.cursor()
        cur.execute('''
            INSERT INTO Polsek VALUES ('%s','%s','%s')
        ''' % data)
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('polsek'))
    else:
        return render_template('polsek/polsekAdd.html', title='Tambah Polsek', submenu='dataPolsek' ,link1='Data Polsek', link2='Tambah Data Polsek', link3='polsek/')


@app.route('/polsek/<kodePolsek>/ubah/', methods=['GET','POST'])
def polsekEdit(kodePolsek):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Polsek WHERE kodePolsek='%s' " % kodePolsek)
    data = cur.fetchone()
    if request.method == 'POST':
        kdPolsek = request.form['kdPolsek']
        namaPolsek = request.form['namaPolsek']
        alamat = request.form['alamat']
        cur.execute('''
            UPDATE Polsek SET namapolsek='%s', 
            alamatkantor='%s' WHERE kodepolsek='%s'
        ''' % (namaPolsek, alamat, kdPolsek ))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('polsek'))
    else:
        cur.close()
        print(data[1])
        print(data[2])
        return render_template('polsek/polsekAdd.html', title='Ubah Polsek', submenu='dataPolsek' ,link1='Data Polsek', link2='Ubah Data Polsek', link3='polsek/', data=data)


@app.route('/polsek/<kodePolsek>/hapus/', methods=['GET','POST'])
def polsekDel(kodePolsek):
    cur = mysql.connection.cursor()
    cur.execute('''
        DELETE FROM Polsek WHERE kodePolsek='%s'
    ''' % kodePolsek)
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('polsek'))

# Akhir Polsek


# Awal MedcenITS
@app.route('/medcen/')
def medcen():
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM MedcenITS;
    ''')
    data = []
    for nrp,alamatMed in cur.fetchall():
        data.append((nrp,alamatMed))
    cur.close()
    print(data)
    return render_template('medcen/medcen.html', title='MedcenITS', submenu='dataMedcenITS', link1='Data MedcenITS' ,data=data)

@app.route('/medcen/tambah/', methods=['GET','POST'])
def medcenAdd():
    if request.method == 'POST':
        nrp = request.form['nrp']
        alamat = request.form['alamat']
        data = (nrp, alamat)
        cur = mysql.connection.cursor()
        cur.execute('''
            INSERT INTO MedcenITS VALUES ('%s','%s')
        ''' % data)
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('medcen'))
    else:
        return render_template('medcen/medcenAdd.html', title='Tambah MedcenITS', submenu='dataMedcenITS' ,link1='Data MedcenITS', link2='Tambah Data Polsek', link3='medcen/')


@app.route('/medcen/<nrp>/ubah/', methods=['GET','POST'])
def medcenEdit(nrp):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM MedcenITS WHERE nrp='%s' " % nrp)
    data = cur.fetchone()
    if request.method == 'POST':
        nrp = request.form['nrp']
        alamat = request.form['alamat']
        cur.execute('''
            UPDATE MedcenITS SET alamatKantor='%s' WHERE nrp='%s'
        ''' % (alamat, nrp))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('medcen'))
    else:
        cur.close()
        return render_template('medcen/medcenAdd.html', title='Ubah Medcen ITS', submenu='dataMedcenITS' ,link1='Data Medcen ITS', link2='Ubah Data MedcenITS', link3='medcen/', data=data)


@app.route('/medcen/<nrp>/hapus/', methods=['GET','POST'])
def delMedcen(nrp):
    cur = mysql.connection.cursor()
    cur.execute('''
        DELETE FROM MedcenITS WHERE nrp='%s'
    ''' % nrp)
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('medcen'))

# Akhir MedcenITS


# Awal Prosedur
@app.route('/prosedur/')
def prosedur():
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM ProsedurLapor;
    ''')
    data = []
    for kd,pLp,pLm in cur.fetchall():
        data.append((kd,pLp,pLm))
    cur.close()
    print(data)
    return render_template('prosedur/prosedur.html', title='Prosedur Lapor', submenu='dataProsedur Lapor', link1='Data Prosedur Lapor' ,data=data)



@app.route('/prosedur/tambah/', methods=['GET','POST'])
def prosedurAdd():
    if request.method == 'POST':
        kdPolsek = request.form['kdPolsek']
        laporPolsek = request.form['laporPolsek']
        laporMedcen = request.form['laporMedcen']
        data = (kdPolsek, laporPolsek, laporMedcen)
        cur = mysql.connection.cursor()
        cur.execute('''
            INSERT INTO ProsedurLapor VALUES ('%s','%s','%s')
        ''' % data)
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('prosedur'))
    else:
        return render_template('prosedur/prosedurAdd.html', title='Tambah Prosedur Lapor', submenu='dataProsedur Lapor' ,link1='Data Prosedur Lapor', link2='Tambah Data Prosedur', link3='prosedur/')

@app.route('/prosedur/<kodePolsek>/hapus/', methods=['GET','POST'])
def delProsedur(kodePolsek):
    cur = mysql.connection.cursor()
    cur.execute('''
        DELETE FROM ProsedurLapor WHERE kodePolsek='%s'
    ''' % kodePolsek)
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('prosedur'))


# Akhir Prosedur


# Awal nLayanan
@app.route('/nomor_layanan/')
def layanan():
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM NomorLayanan;
    ''')
    data = []
    for kd,nLp,nLm,nDp in cur.fetchall():
        data.append((kd,nLp,nLm,nDp))
    cur.close()
    print(data)
    return render_template('nomorlayanan/nLayanan.html', title='Nomor Layanan', submenu='dataNomor Layanan', link1='Data Nomor Layanan' ,data=data)

@app.route('/nomor_layanan/tambah/', methods=['GET','POST'])
def layananAdd():
    if request.method == 'POST':
        kdPolsek = request.form['kdPolsek']
        lPolsek = request.form['layananPolsek']
        dPolsek = request.form['daruratPolsek']
        lMedcen = request.form['layananMedcen']
        data = (kdPolsek, lPolsek, dPolsek, lMedcen)
        cur = mysql.connection.cursor()
        cur.execute('''
            INSERT INTO NomorLayanan VALUES ('%s','%s','%s','%s')
        ''' % data)
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('layanan'))
    else:
        return render_template('nomorlayanan/nLayananAdd.html', title='Tambah Nomor Layanan', submenu='dataNomor Layanan' ,link1='Data Nomor Layanan', link2='Tambah Data Nomor Layanan', link3='nomor_layanan/')


@app.route('/layanan/<kodePolsek>/ubah/', methods=['GET','POST'])
def layananEdit(kodePolsek):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM NomorLayanan WHERE kodePolsek='%s' " % kodePolsek)
    data = cur.fetchone()
    if request.method == 'POST':
        kodePolsek = request.form['kdPolsek']
        lPolsek = request.form['layananPolsek']
        dPolsek = request.form['daruratPolsek']
        lMedcen = request.form['layananMedcen']
        cur.execute('''UPDATE NomorLayanan SET NomorLayananPolsek='%s', 
                    NomorDaruratPolsek='%s', NomorLayananMedcen='%s', WHERE kodePolsek='%s'
        ''' % (kodePolsek, lPolsek, dPolsek, lMedcen))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('layanan'))
    else:
        cur.close()
        return render_template('nomorlayanan/nLayananAdd.html', title='Ubah Nomor Layanan', submenu='dataNomor Layanan' ,link1='Data Nomor Layanan', link2='Ubah Data Nomor Layanan', link3='nomor_layanan/', data=data)


@app.route('/layanan/<kodePolsek>/hapus/', methods=['GET','POST'])
def layananDel(kodePolsek):
    cur = mysql.connection.cursor()
    cur.execute('''
        DELETE FROM NomorLayanan WHERE kodePolsek='%s'
    ''' % kodePolsek)
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('layanan'))

# Akhir nLayanan


# Awal WebResmi
@app.route('/website_resmi/')
def webResmi():
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM WebsiteResmi;
    ''')
    data = []
    for kd,WebsiteResmiPol,WebsiteResmiMed in cur.fetchall():
        data.append((kd,WebsiteResmiPol,WebsiteResmiMed))
    cur.close()
    print(data)
    return render_template('webResmi/webResmi.html', title='Data Website Resmi', submenu='dataWebsite Resmi', link1='Data Web Resmi' ,data=data)

@app.route('/website_resmi/tambah/', methods=['GET','POST'])
def webResmiAdd():
    if request.method == 'POST':
        kdPolsek = request.form['kdPolsek']
        webPolsek = request.form['webPolsek']
        webMedcen = request.form['webMedcen']
        data = (kdPolsek, webPolsek, webMedcen)
        cur = mysql.connection.cursor()
        cur.execute('''
            INSERT INTO WebsiteResmi VALUES ('%s','%s','%s')
        ''' % data)
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('webResmi'))
    else:
        return render_template('webResmi/webResmiAdd.html', title='Tambah Website Resmi', submenu='dataWebsite Resmi' ,link1='Data Website Resmi', link2='Tambah Data Website Resmi', link3='website_resmi/')

@app.route('/website_resmi/<kodePolsek>/ubah/', methods=['GET','POST'])
def webResmiEdit(kodePolsek):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM WebsiteResmi WHERE kodePolsek='%s' " % kodePolsek)
    data = cur.fetchone()
    if request.method == 'POST':
        kodePolsek = request.form['kdPolsek']
        webMedcen = request.form['webMedcen']
        webPolsek = request.form['webPolsek']
        cur.execute('''UPDATE WebsiteResmi SET WebsiteResmiMedcen='%s', 
                    WebsiteResmiPolsek='%s' WHERE kodePolsek='%s'
        ''' % (webMedcen,webPolsek,kodePolsek))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('webResmi'))
    else:
        cur.close()
        return render_template('webResmi/webResmiAdd.html', title='Ubah Website Resmi', submenu='dataWebsite Resmi' ,link1='Data Website Resmi', link2='Ubah Data Website Resmi', link3='website_resmi/', data=data)


@app.route('/website_resmi/<kodePolsek>/hapus/', methods=['GET','POST'])
def webResmiDel(kodePolsek):
    cur = mysql.connection.cursor()
    cur.execute('''
        DELETE FROM WebsiteResmi WHERE kodePolsek='%s'
    ''' % kodePolsek)
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('webResmi'))

# Akhir WebResmi




# Awal DataLapor
@app.route('/data_lapor/')
def dataLapor():
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM DataLapor;
    ''')
    data = []
    for nama,kejadian,nophone,lBer in cur.fetchall():
        data.append((nama,kejadian,nophone,lBer))
    cur.close()
    print(data)
    return render_template('dataLapor/lapor.html', title='Data Lapor', submenu='data Lapor', link1='Data Lapor' ,data=data)

@app.route('/data_lapor/tambah/', methods=['GET','POST'])
def dataLaporAdd():
    if request.method == 'POST':
        nama = request.form['nama']
        kejadian = request.form['kejadian']
        nophone = request.form['nophone']
        lembaga = request.form['lembaga']
        data = (nama, kejadian, nophone, lembaga)
        cur = mysql.connection.cursor()
        cur.execute('''
            INSERT INTO DataLapor VALUES ('%s','%s','%s','%s')
        ''' % data)
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('dataLapor'))
    else:
        return render_template('dataLapor/laporAdd.html', title='Tambah Data Lapor', submenu='data Lapor' ,link1='Data Lapor ', link2='Tambah Data Lapor ', link3='data_lapor/')


@app.route('/data_lapor/<nomorhp>/ubah/', methods=['GET','POST'])
def dataLaporEdit(nomorhp):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM DataLapor WHERE nomorhp='%s' " % nomorhp)
    data = cur.fetchone()
    if request.method == 'POST':
        nama = request.form['nama']
        kejadian = request.form['kejadian']
        nophone = request.form['nophone']
        lembaga = request.form['lembaga']
        cur.execute('''UPDATE DataLapor SET nama='%s', kejadian='%s', 
                 lembagaBerwenang='%s' WHERE nomorhp='%s'
        ''' % (nama, kejadian, lembaga, nophone,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('dataLapor'))
    else:
        cur.close()
        return render_template('dataLapor/laporAdd.html', title='Ubah Data Lapor', submenu='data Lapor' ,link1='Data Lapor ', link2='Ubah Data Lapor ', link3='data_lapor/', data=data)


@app.route('/data_lapor/<nomorhp>/hapus/', methods=['GET','POST'])
def dataLaporDel(nomorhp):
    cur = mysql.connection.cursor()
    cur.execute(" DELETE FROM DataLapor WHERE nomorhp='%s' " % nomorhp)
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('dataLapor'))


# Akhir DataLapor
