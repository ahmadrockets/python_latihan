import MySQLdb as mdb
import sys

db  = mdb.connect('localhost', 'root', '', 'python')
cur = db.cursor()

try:
    sql = "insert"
except :
    print("Gagal insert data")

if db:
    db.close()