#!/usr/bin/python3.10.5

"""
    A script lists that lists all states of
    database htbn_0e_0_usa starting with letter N
"""

import sys, MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM states\
               WHERE name LIKE BINARY 'N%'\
               ORDER BY id ASC")
data = cursor.fetchall()
for row in data:
    print(row)
cursor.close()
db.close()
