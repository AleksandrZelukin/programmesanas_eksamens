import sqlite3

conn=sqlite3.connect('ofice.db')
cur=conn.cursor()

cur.execute('''
CREATE TABLE if NOT EXISTS darbinieks (
    id_darbinieks TEXT PRIMARY KEY,
    vards TEXT,
    uzvards TEXT,
    alga REAL,
    atvalinajums TEXT
)
''')


# cur.execute('''INSERT OR IGNORE INTO darbinieks (id_darbinieks, vards, uzvards, atvalinajums) VALUES
#     ('121278-11234', 'Janis', 'Berzins', 'N'),
#     ('110367-11234', 'Anna', 'Ozola', 'N'),
#     ('090997-11234', 'Pēteris', 'Kalniņš', 'Y')
# ''')

# cur.execute('''UPDATE darbinieks SET atvalinajums = 'Y' where id_darbinieks = '110367-11234' ''')



cur.execute('''SELECT * FROM darbinieks WHERE atvalinajums = 'Y' ''')
rows = cur.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()
