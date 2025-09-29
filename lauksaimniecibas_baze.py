import sqlite3

conn=sqlite3.connect('lauksaimniecibas_baze.db')
cur=conn.cursor()

cur.execute('''DROP TABLE IF EXISTS saimnieks''')
cur.execute('''DROP TABLE IF EXISTS produkts''')
cur.execute('''DROP TABLE IF EXISTS piegade''')

cur.execute('''CREATE TABLE if NOT EXISTS saimnieks
            (id_saimnieks INTEGER PRIMARY KEY autoincrement,
            vards TEXT,
            uzvards TEXT,
            epasts TEXT)
            ''')
cur.execute('''CREATE TABLE if NOT EXISTS produkts
            (id_produkts INTEGER PRIMARY KEY autoincrement,
            nosaukums TEXT,
            piezimes TEXT)
            ''')
cur.execute('''CREATE TABLE if NOT EXISTS piegade
            (id_piegade INTEGER PRIMARY KEY autoincrement,
            id_saimnieks INTEGER,
            id_produkts INTEGER,
            daudzums REAL,
            cena REAL,
            piegades_datums TEXT,
            FOREIGN KEY (id_saimnieks) REFERENCES saimnieks(id_saimnieks),
            FOREIGN KEY (id_produkts) REFERENCES produkts(id_produkts))
            ''')
cur.executemany('''INSERT OR IGNORE INTO saimnieks (vards, uzvards, epasts) VALUES( ?, ?, ?)''',[
            ('Jānis', 'Bērziņš', 'janis@example.com'),
            ('Anna', 'Ozola', 'anna@pasts.lv'),
            ('Pēteris', 'Kalniņš', 'peteris@pasts.lv'),
            ('Līga', 'Liepa', 'liga@inbox.lv'),
            ('Mārtiņš', 'Ziediņš', 'martins@hotmail.com')])
cur.executemany('''INSERT OR IGNORE INTO produkts (nosaukums, piezimes) VALUES(?, ?)''',[
            ('Āboli', 'Saldie'),
            ('Bumbieri', 'Sulīgie'),
            ('Plūmes', 'Skābenes'),
            ('Zemenes', 'Saldās'),
            ('Mellenes', 'Meža ogas')])
            
cur.executemany('''INSERT OR IGNORE INTO piegade (id_saimnieks, id_produkts, daudzums, cena, piegades_datums) VALUES(?, ?, ?, ?, ?)''',[
            (1, 1, 100.0, 0.5, '2023-10-01'),
            (2, 2, 150.0, 0.7, '2023-10-02'),
            (3, 3, 200.0, 0.6, '2024-09-03'),
            (4, 4, 120.0, 1.0, '2022-11-04'),
            (5, 5, 80.0, 1.5, '2021-10-05')])
cur.execute('''SELECT saimnieks.vards, saimnieks.uzvards, produkts.nosaukums, piegade.daudzums, piegade.cena, piegade.piegades_datums
            FROM piegade
            JOIN saimnieks ON piegade.id_saimnieks = saimnieks.id_saimnieks
            JOIN produkts ON piegade.id_produkts = produkts.id_produkts
            WHERE piegade.cena > 0.0
            ''')
print("Vārds Uzvārds Produkts Daudzums (kg) Cena (EUR) Piegādes datums")
rows = cur.fetchall()
for row in rows:
    print(" ".join(map(str, row)))

cur.execute('''SELECT SUM(piegade.daudzums), produkts.nosaukums
            FROM piegade
            JOIN produkts ON piegade.id_produkts = produkts.id_produkts
            GROUP BY produkts.nosaukums
            ''')
print("\nKopējais daudzums pēc produkta")
rows = cur.fetchall()
for row in rows:
    print(" ".join(map(str, row)))

cur.execute('''SELECT AVG(piegade.cena), produkts.nosaukums
            FROM piegade
            JOIN produkts ON piegade.id_produkts = produkts.id_produkts
            GROUP BY produkts.nosaukums   
            ''')
print("\nVidējā cena pēc produkta")
rows = cur.fetchall()
for row in rows:
    print(" ".join(map(str, row)))

cur.execute('''SELECT saimnieks.vards, saimnieks.uzvards, piegade.piegades_datums
            FROM piegade
            JOIN saimnieks ON piegade.id_saimnieks = saimnieks.id_saimnieks
            JOIN produkts ON piegade.id_produkts = produkts.id_produkts
            WHERE piegade.piegades_datums > '2023-10-01'
            ''')
print("\nPiegādes pēc datuma")
rows = cur.fetchall()
for row in rows:
    print(" ".join(map(str, row)))
cur.close()
conn.commit()