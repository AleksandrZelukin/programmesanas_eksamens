import sqlite3

conn = sqlite3.connect('gramatas.db')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS gramata (
        id_gramata INTEGER PRIMARY KEY,
        nosaukums TEXT,
        autors TEXT,
        izlaiduma_gads INTEGER,
        isbn TEXT UNIQUE
    )
''')
cur.execute('''
    CREATE TABLE IF NOT EXISTS lasitajs (
        id_lasitajs INTEGER PRIMARY KEY,
        vards TEXT,
        uzvards TEXT,
        talrunis TEXT
    )
''')
cur.execute('''
    CREATE TABLE IF NOT EXISTS lasitava (
        id_lasitava INTEGER PRIMARY KEY,
        id_gramata INTEGER,
        id_lasitajs INTEGER,
        iznemsanas_datums TEXT,
        atgriesanas_datums TEXT,
        FOREIGN KEY (id_gramata) REFERENCES gramata(id_gramata),
        FOREIGN KEY (id_lasitajs) REFERENCES lasitajs(id_lasitajs)
    )
''')

cur.execute('''
    INSERT OR IGNORE INTO gramata (id_gramata, nosaukums, autors, izlaiduma_gads, isbn)
    VALUES (1, '1984', 'George Orwell', 1949, '9780451524935'),
           (2, 'To Kill a Mockingbird', 'Harper Lee', 1960, '9780060935467')
''')
cur.execute('''
    INSERT OR IGNORE INTO lasitajs (id_lasitajs, vards, uzvards, talrunis)
    VALUES (1, 'John', 'Doe', '12345678')
''')
cur.execute('''
    INSERT OR IGNORE INTO lasitava (id_lasitava, id_gramata, id_lasitajs, iznemsanas_datums, atgriesanas_datums)
    VALUES (1, 1, 1, '2023-01-01', '2023-01-15')
''')
conn.commit()
conn.close()