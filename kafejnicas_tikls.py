import sqlite3

conn=sqlite3.connect('kafejnicas_tikls.db')
cur=conn.cursor()

cur.execute('''
CREATE TABLE if NOT EXISTS kafejnica (
    id_kafejnica INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT,
    adrese TEXT,
    talrunis TEXT
)
''')
cur.execute('''
CREATE TABLE if NOT EXISTS darbinieks (
    id_darbinieks INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT,
    uzvards TEXT,
    amats TEXT,
    alga REAL,
    id_kafejnica INTEGER,
    FOREIGN KEY (id_kafejnica) REFERENCES kafejnica(id_kafejnica)
)
''')

cur.execute('''
CREATE TABLE if NOT EXISTS produkts (
    id_produkts INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT,
    cena REAL,
    kategorija TEXT,
    id_darbinieks INTEGER,
    FOREIGN KEY (id_darbinieks) REFERENCES darbinieks(id_darbinieks)
)
''')

# cur.execute('''INSERT INTO kafejnica (nosaukums, adrese, talrunis) VALUES
#     ('Kafejnīca A', 'Rīgas iela 1, Rīga', '+37112345678'),
#     ('Kafejnīca B', 'Brīvības iela 10, Rīga', '+37187654321')
#     ''')
# cur.execute('''INSERT INTO darbinieks (vards, uzvards, amats, alga, id_kafejnica) VALUES
#     ('Jānis', 'Bērziņš', 'Bārmenis', 1200.00, 1),
#     ('Anna', 'Kalniņa', 'Oficiants', 1100.00, 1),
#     ('Pēteris', 'Ozoliņš', 'Šefpavārs', 1500.00, 2)
#     ''')
# cur.execute('''INSERT INTO produkts (nosaukums, cena, kategorija,id_darbinieks) VALUES
#     ('Kafija', 2.50, 'Dzēriens', 1),
#     ('Tēja', 2.00, 'Dzēriens', 1),
#     ('Sviestmaize', 3.50, 'Uzkoda', 2),
#     ('Kūka', 4.00, 'Deserts', 2)
#     ''')

# kaf = input("Ievadi kafejnīcas nosaukumu: ")
# adr = input("Ievadi kafejnīcas adresi: ")
# tal = input("Ievadi kafejnīcas tālruni: ")

# cur.execute('''INSERT INTO kafejnica (nosaukums, adrese, talrunis) VALUES (?, ?, ?)''', (kaf, adr, tal))

# vards = input("Ievadi darbinieka vārdu: ")
# uzvards = input("Ievadi darbinieka uzvārdu: ") 
# amats = input("Ievadi darbinieka amatu: ")
# alga = float(input("Ievadi darbinieka algu: "))
# kafejnica_id = input("Ievadi kafejnīcas ID: ")  # Pieņemam, ka darbinieks strādā pirmajā kafejnīcā
# cur.execute('''INSERT INTO darbinieks (vards, uzvards, amats, alga, id_kafejnica) VALUES (?, ?, ?, ?, ?)''', (vards, uzvards, amats, alga, kafejnica_id))

# nos = input("Ievadi produkta nosaukumu: ")
# cen = float(input("Ievadi produkta cenu: "))
# kat = input("Ievadi produkta kategoriju: ")
# darbinieks_id = input("Ievadi darbinieka ID: ")  # Pieņemam, ka produkts tiek pievienots pirmajam darbiniekam
# cur.execute('''INSERT INTO produkts (nosaukums, cena, kategorija, id_darbinieks) VALUES (?, ?, ?, ?)''', (nos, cen, kat, darbinieks_id))

# cur.execute('SELECT * FROM kafejnica')
# print("Kafejnīcas:")
# for row in cur.fetchall():
#     print(row)
# cur.execute('SELECT * FROM darbinieks')
# print("\nDarbinieki:")
# for row in cur.fetchall():
#     print(row)
# cur.execute('SELECT * FROM produkts')
# print("\nProdukti:")
# for row in cur.fetchall():
#     print(row)
    
cur.execute('''
SELECT kafejnica.nosaukums, darbinieks.vards, darbinieks.uzvards, produkts.nosaukums, produkts.cena
FROM kafejnica 
JOIN darbinieks ON kafejnica.id_kafejnica = darbinieks.id_kafejnica
JOIN produkts ON darbinieks.id_darbinieks = produkts.id_darbinieks
''')
for row in cur.fetchall():
    print(row)
conn.commit()
conn.close()