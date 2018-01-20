import MySQLdb as mdb
import sys

db = mdb.connect('localhost', 'root','','python')
cur = db.cursor()

sql = "UPDATE orang SET nama = '%s' WHERE id = '%s'" % ('Ayunda Sekar Ningrum', '2')

try:
    cur.execute(sql)
    db.commit()
    print ("Update Data Berhasil")
    print (cur._last_executed)
except :
    db.rollback()
    print ("Update Data Gagal")
    print (cur._last_executed)

if db:
    db.close()
