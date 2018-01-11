import MySQLdb as mdb
import sys
import datetime

db  = mdb.connect('localhost', 'root', '', 'python')
cur = db.cursor()

try:
    date = datetime.datetime(1995, 10, 10)
    sql = "INSERT INTO orang (nama, alamat, tgl_lahir) VALUES ('%s', '%s', '%s')" % ('Prasetyo Nugroho', 'Jl Ahmad Yani', date)
    cur.execute(sql)
    db.commit()
    print("Berhasil input data")
    print (cur._last_executed)
except :
    db.rollback()
    print(cur._last_executed)
    print("Gagal insert data")
if db:
    db.close()
