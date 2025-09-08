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

cur.execute('''INSERT INTO kafejnica (nosaukums, adrese, talrunis) VALUES
    ('Kafejnīca A', 'Rīgas iela 1, Rīga', '+37112345678'),
    ('Kafejnīca B', 'Brīvības iela 10, Rīga', '+37187654321')
    ''')
cur.execute('''INSERT INTO darbinieks (vards, uzvards, amats, alga, id_kafejnica) VALUES
    ('Jānis', 'Bērziņš', 'Bārmenis', 1200.00, 1),
    ('Anna', 'Kalniņa', 'Oficiants', 1100.00, 1),
    ('Pēteris', 'Ozoliņš', 'Šefpavārs', 1500.00, 2)
    ''')
cur.execute('''INSERT INTO produkts (nosaukums, cena, kategorija,id_darbinieks) VALUES
    ('Kafija', 2.50, 'Dzēriens', 1),
    ('Tēja', 2.00, 'Dzēriens', 1),
    ('Sviestmaize', 3.50, 'Uzkoda', 2),
    ('Kūka', 4.00, 'Deserts', 2)
    ''')
conn.commit()
conn.close()