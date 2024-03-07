import sqlite3

# Connessione al database
conn = sqlite3.connect('studenti.db')
cursor = conn.cursor()

# Eliminazione di tutte le righe dalla tabella degli studenti
cursor.execute('DELETE FROM studenti')

# Commit delle modifiche e chiusura della connessione
conn.commit()
conn.close()

print("Contenuto del database cancellato con successo.")
