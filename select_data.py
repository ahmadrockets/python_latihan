import MySQLdb as mdb
import sys

db = mdb.connect('localhost', 'root', '', 'python')
cur = db.cursor()

try:
    sql = "SELECT * FROM orang WHERE id = '%s' " % ('1')
    cur.execute(sql)
    user  = cur.fetchone()
    print ("Nama : %s" % user[1])
except:
    print("Gagal mengambil data dari database")

if db:
    db.close()
