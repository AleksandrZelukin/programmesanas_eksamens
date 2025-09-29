# Veikalam „Brūnaļa” ir nepieciešama datubāze (no savstarpēji saistītajām tabulām), kurā var ērti uzskaitīt no katra klienta 
# (fiziskās personas) iepirktās
# ekoloģiskās produkcijas daudzumu un samaksāto naudu par iepirkumiem.
# Datubāzei jāsatur:
# ● informācija par saimnieku, kurš palīdz ar viņu sadarboties;
# ● informācija par iepērkamajiem produktiem, t. sk. informācija, kad katrs produkts iegādāts, 
# katra produkta cena par kilogramu vai gramiem vai litriem.
# Daži piemēri, kāda var būt iepirktā produkcija:
# ○ piens (govs 2 % 1,32 eiro/litrā vai 2,5 % 1,50 eiro/litrā, vai 3,5 % 1,80 eiro/litrā; kazas piens 3,60 eiro/litrā);
# ○ siers (govs svaigs siers 9 eiro kilogramā, svaigs ar ķimenēm 9,50 eiro kilogramā, auksti kūpināts 13 eiro kilogramā; 
# kazas svaigs 15 eiro kilogramā
# vai auksti kūpināts 17 eiro kilogramā);
# ○ krējums (svaigs govs krējums 7 eiro litrā vai skābais govs krējums 5 eiro litrā).
# Vieta uzglabāšanai: datubāze SQLite3.

# --- Datubāzes inicializācija ---
import sqlite3
from datetime import datetime

# Izveido datubāzi
conn = sqlite3.connect("veikals_brunala.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Klienti")
cur.execute("DROP TABLE IF EXISTS Saimnieki")
cur.execute("DROP TABLE IF EXISTS Produkti")
cur.execute("DROP TABLE IF EXISTS Iepirkumi")

# Tabula par klientiem
cur.execute("""
CREATE TABLE IF NOT EXISTS Klienti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    telefons TEXT
)
""")

# Tabula par saimniekiem
cur.execute("""
CREATE TABLE IF NOT EXISTS Saimnieki (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    saimnieciba TEXT
)
""")

# Tabula par produktiem
cur.execute("""
CREATE TABLE IF NOT EXISTS Produkti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    tips TEXT,
    mer_vieniba TEXT,
    cena REAL NOT NULL,
    saimnieks_id INTEGER,
    FOREIGN KEY (saimnieks_id) REFERENCES Saimnieki(id)
)
""")

# Tabula par iepirkumiem
cur.execute("""
CREATE TABLE IF NOT EXISTS Iepirkumi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    klients_id INTEGER,
    produkts_id INTEGER,
    daudzums REAL NOT NULL,
    datums TEXT NOT NULL,
    samaksa REAL NOT NULL,
    FOREIGN KEY (klients_id) REFERENCES Klienti(id),
    FOREIGN KEY (produkts_id) REFERENCES Produkti(id)
)
""")

# Pievienojam piemēra saimniekus
cur.executemany("""
INSERT INTO Saimnieki (vards, uzvards, saimnieciba) VALUES (?, ?, ?)
""", [
    ("Jānis", "Kalniņš", "Kalna saimniecība"),
    ("Anna", "Bērziņa", "Zaļā pļava")
])

# Pievienojam piemēra produktus
cur.executemany("""
INSERT INTO Produkti (nosaukums, tips, mer_vieniba, cena, saimnieks_id) VALUES (?, ?, ?, ?, ?)
""", [
    ("Piens govs 2%", "piens", "litrs", 1.32, 1),
    ("Piens govs 2.5%", "piens", "litrs", 1.50, 1),
    ("Piens govs 3.5%", "piens", "litrs", 1.80, 1),
    ("Piens kazas", "piens", "litrs", 3.60, 2),
    ("Siers govs svaigs", "siers", "kg", 9.00, 1),
    ("Siers govs ar ķimenēm", "siers", "kg", 9.50, 1),
    ("Siers govs auksti kūpināts", "siers", "kg", 13.00, 1),
    ("Siers kazas svaigs", "siers", "kg", 15.00, 2),
    ("Siers kazas auksti kūpināts", "siers", "kg", 17.00, 2),
    ("Krējums govs svaigs", "krējums", "litrs", 7.00, 1),
    ("Krējums govs skābais", "krējums", "litrs", 5.00, 1)
])

# Pievienojam klientu
cur.execute("""
INSERT INTO Klienti (vards, uzvards, telefons) VALUES (?, ?, ?)
""", ("Pēteris", "Ozols", "+37120000000"))

# Pievienojam pirkumu
cur.execute("""
INSERT INTO Iepirkumi (klients_id, produkts_id, daudzums, datums, samaksa)
VALUES (?, ?, ?, ?, ?)
""", (1, 1, 2, datetime.now().strftime("%Y-%m-%d"), 2 * 1.32))


print("\n--- Kopā samaksājis katrs klients ---")
for row in cur.execute("""
SELECT k.vards || ' ' || k.uzvards AS Klients,
       SUM(i.samaksa) AS Kopā_samaksāts
FROM Iepirkumi i
JOIN Klienti k ON i.klients_id = k.id
GROUP BY k.id
"""):
    print(row)

print("\n--- Visbiežāk pirktie produkti ---")
for row in cur.execute("""
SELECT p.nosaukums,
       SUM(i.daudzums) AS Kopā_daudzums
FROM Iepirkumi i
JOIN Produkti p ON i.produkts_id = p.id
GROUP BY p.id
ORDER BY Kopā_daudzums DESC
"""):
    print(row)

print("\n--- Top produkts pēc ieņēmumiem ---")
for row in cur.execute("""
SELECT p.nosaukums,
       SUM(i.samaksa) AS Ieņēmumi
FROM Iepirkumi i
JOIN Produkti p ON i.produkts_id = p.id
GROUP BY p.id
ORDER BY Ieņēmumi DESC
LIMIT 1
"""):
    print(row)

print("\n--- Ieņēmumi no produktiem pēc saimnieka ---")
for row in cur.execute("""
SELECT s.vards || ' ' || s.uzvards AS Saimnieks,
       p.nosaukums,
       SUM(i.samaksa) AS Ieņēmumi
FROM Iepirkumi i
JOIN Produkti p ON i.produkts_id = p.id
JOIN Saimnieki s ON p.saimnieks_id = s.id
GROUP BY s.id, p.id
ORDER BY Saimnieks, Ieņēmumi DESC
"""):
    print(row)
conn.commit()
conn.close()

