from app import app, mysql
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/dashboard')
def home():
    # Pertama
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM Pribadi;
    ''')
    data = []
    for nrp,ktp,kk,stnk,nama,alamat,nophone in cur.fetchall():
        data.append((nrp,ktp,kk,stnk,nama,alamat,nophone))
    cur.close()
    print(data)

    # Kedua
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM Polsek;
    ''')
    data2 = []
    for kd,ktp,alamatPol,namaPol in cur.fetchall():
        data2.append((kd,ktp,alamatPol,namaPol))
    cur.close()
    print(data2)

    # Ketiga
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM MedcenITS;
    ''')
    data3 = []
    for ktp,alamatKantor in cur.fetchall():
        data3.append((ktp,alamatKantor))
    cur.close()
    print(data3)
    return render_template('index.html', title='Dashboard', menu='dashboard', data=data, data2=data2, data3=data3)

@app.route('/pribadi/')
def pribadi():
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM Pribadi;
    ''')
    data = []
    for nrp,ktp,kk,stnk,nama,alamat,nophone in cur.fetchall():
        data.append((nrp,ktp,kk,stnk,nama,alamat,nophone))
    cur.close()
    print(data)
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
        data = (nrp, ktp, kk, stnk, nama, alamat, nophone)
        cur = mysql.connection.cursor()
        cur.execute('''
            INSERT INTO Pribadi VALUES ('%s','%s','%s','%s','%s','%s','%s')
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
    return redirect(url_for('dashboard'))