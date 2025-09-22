import sqlite3

# Izveidojam savienojumu ar datubāzi (failā vai atmiņā)
conn = sqlite3.connect("saimniecibas_veikals.db")
cur = conn.cursor()

# Dzēšam tabulas, ja tās jau eksistē
cur.execute("DROP TABLE IF EXISTS piegadataji") #ekzistējošo tabulu dzēšana, lai varētu izveidot no jauna
cur.execute("DROP TABLE IF EXISTS produkti")
cur.execute("DROP TABLE IF EXISTS cenas")
cur.execute("DROP TABLE IF EXISTS iepirkumi")

# Piegādātāji - uzņēmumi vai personas, kas piegādā produkciju
cur.execute("""
CREATE TABLE IF NOT EXISTS piegadataji (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    kontakts TEXT
)
""")

# Produkti - veikalā pieejamās lauksaimniecības preces
cur.execute("""
CREATE TABLE IF NOT EXISTS produkti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    kategorija TEXT
)
""")

# Cenas - konkrēta piegādātāja piedāvātā produkta cena
cur.execute("""
CREATE TABLE IF NOT EXISTS cenas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produkta_id INTEGER,
    piegadataja_id INTEGER,
    cena REAL NOT NULL,
    FOREIGN KEY (produkta_id) REFERENCES produkti(id),
    FOREIGN KEY (piegadataja_id) REFERENCES piegadataji(id)
)
""")

# Iepirkumi - veikala veiktie pirkumi no piegādātājiem
cur.execute("""
CREATE TABLE IF NOT EXISTS iepirkumi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produkta_id INTEGER,
    piegadataja_id INTEGER,
    daudzums INTEGER,
    datums TEXT,
    FOREIGN KEY (produkta_id) REFERENCES produkti(id),
    FOREIGN KEY (piegadataja_id) REFERENCES piegadataji(id)
)
""")

# Pievienojam piemēra datus
cur.executemany("INSERT INTO piegadataji (nosaukums, kontakts) VALUES (?, ?)", [
    ("Lauku Ferma                           ", "ferma@example.com"),
    ("Bioloģiskā saimniecība                ", "bio@example.com"),
    ("Zemnieku saimniecība Kalni            ", "kalni@example.com"),
    ("Dārzeņu audzētājs Sētas               ", "setas@example.com"),
    ("Augļu dārzs Zaļais                    ", "zalais@example.com"),
    ("Piena pārstrādes uzņēmums Piensaimnieks", "piensaimnieks@example.com")
])

cur.executemany("INSERT INTO produkti (nosaukums, kategorija) VALUES (?, ?)", [
    ("Piens.   ", "Piena produkti"),
    ("Siers.   ", "Piena produkti"),
    ("Olas.    ", "Olu produkti"),
    ("Gaļa.    ", "Gaļas produkti"),
    ("Dārzeņi. ", "Dārzeņu produkti"),
    ("Augļi.   ", "Augļu produkti"),
    ("Maize.   ", "Maizes izstrādājumi"),
    ("Medus.   ", "Citi produkti"),
    ("Saldējums", "Citi produkti"),
    ("Jogurts. ", "Piena produkti")
])

cur.executemany("INSERT INTO cenas (produkta_id, piegadataja_id, cena) VALUES (?, ?, ?)", [
    (1, 1, 1.20),  # Piens no Lauku Ferma
    (1, 2, 1.10),  # Piens no Bioloģiskā saimniecība
    (2, 1, 5.50),  # Siers no Lauku Ferma
    (2, 3, 5.20),  # Siers no Kalni
    (3, 2, 2.80),  # Olas no Bioloģiskā saimniecība
    (4, 3, 7.00),  # Gaļa no Kalni
    (5, 4, 1.50),  # Dārzeņi no Sētas
    (6, 5, 2.00),  # Augļi no Zaļais
    (7, 1, 1.00),  # Maize no Lauku Ferma
    (8, 6, 6.00),  # Medus no Piensaimnieks
    (9, 6, 3.50),  # Saldējums no Piensaimnieks
    (10, 2, 0.80)  # Jogurts no Bioloģiskā saimniecība
    
])

cur.executemany("INSERT INTO iepirkumi (produkta_id, piegadataja_id, daudzums, datums) VALUES (?, ?, ?, ?)", [
    (1, 2, 100, "2025-09-01"),  # 100 litri piena no Bioloģiskā saimniecība
    (2, 1, 20, "2025-09-05"),   # 20 kg siera no Lauku Ferma
    (3, 2, 200, "2025-09-10"),  # 200 olas no Bioloģiskā saimniecība
    (4, 3, 50, "2025-09-12"),     # 50 kg gaļas no Kalni
    (5, 4, 150, "2025-09-15"),  # 150 kg dārzeņu no Sētas
    (6, 5, 100, "2025-09-18"),  # 100 kg augļu no Zaļais
    (7, 1, 80, "2025-09-20"),   # 80 maizes klaipi no Lauku Ferma
    (8, 6, 30, "2025-09-22"),   # 30 kg medus no Piensaimnieks
    (9, 6, 40, "2025-09-25"),   # 40 litri saldējums no Piensaimnieks
    (10, 2, 120, "2025-09-28")  # 120 jogurta burciņas no Bioloģiskā saimniecība
])

# Saglabājam izmaiņas
conn.commit()

print("Datubāze un tabulas izveidotas veiksmīgi ar piemēra datiem.")

# Aizveram savienojumu

cur.execute('''SELECT piegadataji.nosaukums, produkti.nosaukums, cenas.cena, iepirkumi.daudzums 
            FROM piegadataji, produkti, cenas, iepirkumi 
            WHERE piegadataji.id = cenas.piegadataja_id 
            AND produkti.id = cenas.produkta_id 
            AND iepirkumi.produkta_id = produkti.id 
            AND iepirkumi.piegadataja_id = piegadataji.id''')
print("Iepirkumu saraksts:")
print("Piegādātājs                             | Produkts | Cena | Daudzums")
rows = cur.fetchall()
for row in rows:
    print(" | ".join(map(str, row)))
conn.close()
