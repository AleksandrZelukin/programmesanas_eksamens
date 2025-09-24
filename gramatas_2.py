import sqlite3
from datetime import date

# Savienojums ar datu bāzi (ja fails neeksistē, tas tiks izveidots)
conn = sqlite3.connect("gramatas_2.db")
cur = conn.cursor()
# Notīrām iepriekšējās tabulas (ja tādas ir)
cur.execute("DROP TABLE IF EXISTS lasitaji;")
cur.execute("DROP TABLE IF EXISTS gramatas;")
cur.execute("DROP TABLE IF EXISTS izsniegumi;")

# --- Tabulu izveide ---
cur.execute("""
CREATE TABLE IF NOT EXISTS lasitaji (
    lasitaja_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    telefons TEXT
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS gramatas (
    gramatas_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    autors TEXT NOT NULL,
    gads INTEGER,
    pieejama INTEGER DEFAULT 1   -- 1 = pieejama, 0 = izsniegta
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS izsniegumi (
    izsnieguma_id INTEGER PRIMARY KEY AUTOINCREMENT,
    lasitaja_id INTEGER NOT NULL,
    gramatas_id INTEGER NOT NULL,
    izsniegts DATE NOT NULL,
    atgriezts DATE,
    FOREIGN KEY(lasitaja_id) REFERENCES lasitaji(lasitaja_id),
    FOREIGN KEY(gramatas_id) REFERENCES gramatas(gramatas_id)
);
""")


conn.commit()

# --- Funkcijas darbam ar bibliotēku ---

def pievienot_lasitaju(vards, telefons=None):
    cur.execute("INSERT INTO lasitaji (vards, telefons) VALUES (?, ?)", (vards, telefons))
    conn.commit()

def pievienot_gramatu(nosaukums, autors, gads):
    cur.execute("INSERT INTO gramatas (nosaukums, autors, gads) VALUES (?, ?, ?)", (nosaukums, autors, gads))
    conn.commit()

def izsniegt_gramatu(lasitaja_id, gramatas_id):
    # Pārbaudām, vai grāmata ir pieejama
    cur.execute("SELECT pieejama FROM gramatas WHERE gramatas_id = ?", (gramatas_id,))
    rezultats = cur.fetchone()
    if not rezultats:
        print("Grāmata ar šādu ID nav atrasta.")
        return
    if rezultats[0] == 0:
        print("Grāmata jau ir izsniegta!")
        return

    # Reģistrējam izsniegumu
    cur.execute("INSERT INTO izsniegumi (lasitaja_id, gramatas_id, izsniegts) VALUES (?, ?, ?)",
                (lasitaja_id, gramatas_id, date.today()))
    # Mainām statusu uz "izsniegta"
    cur.execute("UPDATE gramatas SET pieejama = 0 WHERE gramatas_id = ?", (gramatas_id,))
    conn.commit()
    print("Grāmata veiksmīgi izsniegta!")

def atgriezt_gramatu(gramatas_id):
    # Atzīmējam atgriešanu
    cur.execute("UPDATE izsniegumi SET atgriezts = ? WHERE gramatas_id = ? AND atgriezts IS NULL",
                (date.today(), gramatas_id))
    # Mainām statusu uz "pieejama"
    cur.execute("UPDATE gramatas SET pieejama = 1 WHERE gramatas_id = ?", (gramatas_id,))
    conn.commit()
    print("Grāmata atgriezta!")

# --- Atskaites vaicājumi ---

def gramatnas_pie_lasitajiem():
    print("\n--- Grāmatas, kas šobrīd ir izsniegtas ---")
    cur.execute("""
    SELECT g.nosaukums, g.autors, l.vards, i.izsniegts
    FROM izsniegumi i
    JOIN gramatas g ON i.gramatas_id = g.gramatas_id
    JOIN lasitaji l ON i.lasitaja_id = l.lasitaja_id
    WHERE i.atgriezts IS NULL
    """)
    for row in cur.fetchall():
        print(row)

def pieejamas_gramatas():
    print("\n--- Pieejamās grāmatas ---")
    cur.execute("SELECT nosaukums, autors, gads FROM gramatas WHERE pieejama = 1")
    for row in cur.fetchall():
        print(row)

def lasitaja_vesture(lasitaja_id):
    print(f"\n--- Lasītāja {lasitaja_id} izsniegumu vēsture ---")
    cur.execute("""
    SELECT g.nosaukums, g.autors, i.izsniegts, i.atgriezts
    FROM izsniegumi i
    JOIN gramatas g ON i.gramatas_id = g.gramatas_id
    WHERE i.lasitaja_id = ?
    """, (lasitaja_id,))
    for row in cur.fetchall():
        print(row)


# --- Lietošanas piemērs ---
if __name__ == "__main__":
    # Pievienojam lasītājus
    pievienot_lasitaju("Jānis Bērziņš", "1234567")
    pievienot_lasitaju("Anna Kalniņa", "9876543")
    pievienot_lasitaju("Pēteris Ozols", "5551234")
    pievienot_lasitaju("Līga Liepa", "4445678")
    pievienot_lasitaju("Marta Ziediņa", "3338765")
    pievienot_lasitaju("Andris Jansons", "2223456")
    pievienot_lasitaju("Ilze Sproģe", "1112345")
    pievienot_lasitaju("Kārlis Vītols", "6667890")
    pievienot_lasitaju("Zane Eglīte", "7778901")
    pievienot_lasitaju("Māris Kalniņš", "8889012")

    # Pievienojam grāmatas no latviešu literatūras
    pievienot_gramatu("Mērnieku laiki", "Reinis un Matīss Kaudzītes", 1879)
    pievienot_gramatu("Pūt, vējiņi!", "Rūdolfs Blaumanis", 1913)
    pievienot_gramatu("Zeme", "Edvarts Virza", 1933)
    pievienot_gramatu("Lāčplēsis", "Andrejs Pumpurs", 1888)
    pievienot_gramatu("Indulis un Ārija", "Rainis", 1912)
    pievienot_gramatu("Skroderdienas Silmačos", "Rūdolfs Blaumanis", 1902)
    pievienot_gramatu("Dvēseļu putenis", "Rainis", 1918)
    pievienot_gramatu("Nāves ēnā", "Jānis Jaunsudrabiņš", 1914)
    pievienot_gramatu("Sidraba šķidrauts", "Anna Brigadere", 1914)
    pievienot_gramatu("Cilvēka bērns", "Jānis Poruks", 1891)
    

    # Izsniegšana
    izsniegt_gramatu(1, 1)   # Jānis paņem "Mērnieku laiki"
    izsniegt_gramatu(2, 1)   # mēģinām vēlreiz izsniegt to pašu -> kļūda
    izsniegt_gramatu(2, 3)   # Anna paņem "Zeme"
    izsniegt_gramatu(3, 5)   # Pēteris paņem "Indulis un Ārija"
    izsniegt_gramatu(4, 2)   # Līga paņem "Pūt, vējiņi!"
    izsniegt_gramatu(5, 4)   # Marta paņem "Lāčplēsis"
    izsniegt_gramatu(6, 6)   # Andris paņem "Skroderdienas Silmačos"
    izsniegt_gramatu(7, 7)   # Ilze paņem "Dvēseļu putenis"
    izsniegt_gramatu(8, 8)   # Kārlis paņem "Nāves ēnā"

    # Atskaites
    gramatnas_pie_lasitajiem()
    pieejamas_gramatas()
    lasitaja_vesture(1)

    # Atgriežam grāmatu
    atgriezt_gramatu(1)

    # Atkal pārbaudām
    pieejamas_gramatas()
    
