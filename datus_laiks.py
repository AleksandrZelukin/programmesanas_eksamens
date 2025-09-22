import sqlite3
import datetime

# Izveidojam savienojumu ar datubāzi (failā vai atmiņā)
conn = sqlite3.connect("datus_laiks.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS datumi_laiki")

# Izveidojam tabulu datumi_laiki
cur.execute('''create table if not exists datumi_laiki (
    id integer primary key autoincrement, 
    datums text, 
    nosaukums text)''')

# Pievienojam piemēra datus
cur.executemany("insert into datumi_laiki (datums, nosaukums) values (?, ?)", [
    ("2023-10-01", "Ražas svētki"),
    ("2023-12-24", "Ziemassvētku vakars"),
    ("2024-01-01", "Jaunais gads"),
    ("2024-02-14", "Valentīndiena"),
    ("2024-03-17", "Īrijas nacionālais diena"),
    ])

cur.execute("SELECT nosaukums, datums FROM datumi_laiki where datums >= '2024-01-01'")

rows = cur.fetchall()
for row in rows:
    print(row)
    
conn.commit()
conn.close()