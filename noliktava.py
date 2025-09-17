import sqlite3
import datetime
conn=sqlite3.connect('noliktava.db')
cur=conn.cursor()
cur.execute('''CREATE TABLE if NOT EXISTS prece (
    id_prece INTEGER PRIMARY KEY autoincrement,
    nosaukums TEXT,
    daudzums INTEGER,
    cena REAL,
    piegadatajs TEXT,
    iepirkuma_datums TEXT,
    iepirkuma_laiks TEXT
)''')
cur.execute('''INSERT OR IGNORE INTO prece (id_prece, nosaukums, daudzums, cena, piegadatajs, iepirkuma_datums, iepirkuma_laiks) VALUES
    (1, 'burkans', 100, 0.50, 'SIA Agro', '2024-01-15', '10:00:00'),
    (2, 'kartupelis', 200, 0.30, 'SIA Agro', '2024-01-10', '11:00:00'),
    (3, 'sinepes', 50, 1.20, 'SIA Garšvielas', '2024-02-01', '12:00:00')
''')
cur.execute('''UPDATE prece SET daudzums = daudzums - 20, 
            iepirkuma_datums = ?, iepirkuma_laiks = ? WHERE id_prece = 1 ''', (datetime.date.today().isoformat(), datetime.datetime.now().time().isoformat()))
cur.execute('''UPDATE prece SET daudzums = daudzums - 50, 
            iepirkuma_datums = ? WHERE id_prece = 2 ''', (datetime.date.today().isoformat(),))
cur.execute('''SELECT * FROM prece WHERE daudzums < 100 ''')
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()

datetime.date.today().isoformat() # '2024-02-15'            
# datetime module is used to get the current date in ISO format (YYYY-MM-DD)
# datetime.date.today() returns the current date
# .isoformat() converts the date to a string in ISO format
# datetime module is part of the Python standard library and does not require separate installation
# The code updates the 'iepirkuma_datums' field to the current date when the quantity of an item is reduced
# The code selects and prints all items where the quantity is less than 100
# The code creates a table 'prece' (item) with fields for item ID, name, quantity, price, supplier, and purchase date
# time format hh:mm:ss
# date format yyyy-mm-dd