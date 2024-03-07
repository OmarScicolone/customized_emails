import sqlite3

# Lista dei nomi degli studenti da inserire nel database
nomi_studenti = [
    ('Mario Mariottide', 's000000@example.com'),
    ('Oscar Carogna', 's111111@example.com'),
    ('Massimo Domani', 's222222@example.com'),
    ('Salvo Errori', 's333333@example.com')
]

# Connessione al database
conn = sqlite3.connect('studenti.db')
cursor = conn.cursor()

# Inserimento dei nomi degli studenti nel database
for nome, email in nomi_studenti:
    cursor.execute('INSERT INTO studenti (nome, email) VALUES (?, ?)', (nome, email))

# Commit delle modifiche e chiusura della connessione
conn.commit()
conn.close()

print("Studenti inseriti nel database con successo")
