import sqlite3

conn=sqlite3.connect('kafejnicas_tikls.db')
cur=conn.cursor()

def create_tables():
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

def ievad_datus_kafejnica():
    kaf = input("Ievadi kafejnīcas nosaukumu: ")
    adr = input("Ievadi kafejnīcas adresi: ")
    tal = input("Ievadi kafejnīcas tālruni: ")
def ievad_datus_darbinieki():
    vards = input("Ievadi darbinieka vārdu: ")
    uzvards = input("Ievadi darbinieka uzvārdu: ")
    amats = input("Ievadi darbinieka amatu: ")
    alga = float(input("Ievadi darbinieka algu: "))
    kafejnica_id = input("Ievadi kafejnīcas ID: ")  # Pieņemam, ka darbinieks strādā pirmajā kafejnīcā
    cur.execute('''INSERT INTO darbinieks (vards, uzvards, amats, alga, id_kafejnica) VALUES (?, ?, ?, ?, ?)''', (vards, uzvards, amats, alga, kafejnica_id))
    cur.execute("SELECT * FROM darbinieks")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.commit()
def ievad_datus_produkti():
    nos = input("Ievadi produkta nosaukumu: ")
    cen = float(input("Ievadi produkta cenu: "))
    kat = input("Ievadi produkta kategoriju: ")
    darbinieks_id = input("Ievadi darbinieka ID: ")

def print_kafejnicas():
    cur.execute("SELECT * FROM kafejnica")
    for row in cur.fetchall():
        print(row) 
        

while True:
    print("Ko vēlies darīt?")
    print("1 - Izveidot tabulas")
    print("2 - Ievadīt datus kafejnīcā")
    print("3 - Ievadīt datus darbiniekā")
    print("4 - Ievadīt datus produktā")
    print("5 - Iziet")

    choice = input("Ievadi izvēli (1-5): ")
    if choice == '1':
        create_tables()
    elif choice == '2':
        print_kafejnicas()
        ievad_datus_kafejnica()
    elif choice == '3':
        ievad_datus_darbinieki()
    elif choice == '4':
        ievad_datus_produkti()
    elif choice == '5':
        break
    else:
        print("Nederīga izvēle.") 
        

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