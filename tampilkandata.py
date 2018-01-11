import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', '', 'python')
cur = con.cursor()

try:
    sql = "SELECT * FROM orang"
    cur.execute(sql)
    orang = cur.fetchall()  
    
    for row in orang:
        id          = row[0]
        nama        = row[1]
        alamat      = row[2]
        tgl_lahit   = row[3]
        print('Nama : %s' % nama)
        print('Alamat : %s' % alamat)

except :
    print('Gagal menampilkan data dari database')

if con:
    con.close()
