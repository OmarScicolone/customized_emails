import sqlite3

# Connessione al database
conn = sqlite3.connect('studenti.db')
cursor = conn.cursor()

# Selezione di tutti gli studenti nel database
cursor.execute('SELECT * FROM studenti')
studenti = cursor.fetchall()

# Stampa dei risultati
print("Contenuto del database:")
for studente in studenti:
    print(studente)

# Chiusura della connessione
conn.close()