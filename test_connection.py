import MySQLdb
import sys

try:
    db = MySQLdb.connect('localhost', 'root', '', 'python')
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print("Database Version %s" % data)
except MySQLdb.Error as e:
    print ("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)
finally :
    if db:
      db.close()
