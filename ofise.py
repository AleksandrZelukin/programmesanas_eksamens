import sqlite3

conn=sqlite3.connect('ofice.db')
cur=conn.cursor()

cur.execute('''CREATE TABLE if NOT EXISTS organizacija (
    id_organizacija INTEGER PRIMARY KEY autoincrement,
    nosaukums TEXT)
''')

cur.execute('''
CREATE TABLE if NOT EXISTS darbinieks (
    id_darbinieks TEXT PRIMARY KEY,
    vards TEXT,
    uzvards TEXT,
    alga REAL,
    atvalinajums TEXT,
    id_organizacija INTEGER,
    FOREIGN KEY (id_organizacija) REFERENCES organizacija(id_organizacija)
)
''')
cur.execute('''INSERT OR IGNORE INTO organizacija (id_organizacija, nosaukums) VALUES
    (1, 'administracija'),
    (2, 'projects'),
    (3, 'razotne')
''')

cur.execute('''INSERT OR IGNORE INTO darbinieks (id_darbinieks, vards, uzvards, atvalinajums, id_organizacija) VALUES
    ('121278-11234', 'Janis', 'Berzins', 'N', 1),
    ('110367-11234', 'Anna', 'Ozola', 'N', 2),
    ('090997-11234', 'Pēteris', 'Kalniņš', 'N', 3)
''')
# cur.execute('''UPDATE darbinieks SET atvalinajums = 'Y' where id_darbinieks = '121278-11234' 
#             OR id_darbinieks = '090997-11234' ''')
# cur.execute('''UPDATE darbinieks SET alga = 1000 where id_darbinieks = '121278-11234' ''')
# cur.execute('''UPDATE darbinieks SET alga = 2000 where id_darbinieks = '110367-11234' ''')
# cur.execute('''UPDATE darbinieks SET alga = 1200 where id_darbinieks = '090997-11234' ''')


# cur.execute('''SELECT * FROM darbinieks WHERE atvalinajums = 'N' ''')
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# cur.execute('''SELECT vards, uzvards, alga FROM darbinieks WHERE alga > 1500 ''')
# rows = cur.fetchall()
# for row in rows:
#     print(row)

cur.execute('''SELECT darbinieks.vards, organizacija.nosaukums, darbinieks.alga
            FROM darbinieks, organizacija 
            WHERE darbinieks.id_organizacija = organizacija.id_organizacija
            AND darbinieks.alga > 1500 
            AND darbinieks.id_organizacija = 2 
            AND darbinieks.atvalinajums = 'Y' ''')
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
