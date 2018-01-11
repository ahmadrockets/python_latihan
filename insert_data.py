import MySQLdb as mdb
import sys

db  = mdb.connect('localhost', 'root', '', 'python')
cur = db.cursor()

try:
    sql = ""
except :
    print("Gagal insert data")

if db:
    db.close()