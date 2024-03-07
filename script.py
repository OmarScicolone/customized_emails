import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3

# Funzione per connettersi al database e recuperare gli studenti
def recupera_studenti():
    conn = sqlite3.connect('studenti.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nome, email FROM studenti')
    studenti = cursor.fetchall()
    conn.close()
    return studenti

# Funzione per inviare email
def invia_email(destinatario, oggetto, corpo):
    # Configura i dettagli del mittente
    mittente = 'prova.prova@gmail.com'
    password = 'password'

    # Costruzione del messaggio
    msg = MIMEMultipart()
    msg['From'] = mittente
    msg['To'] = destinatario
    msg['Subject'] = oggetto

    # Aggiunta del corpo del messaggio
    msg.attach(MIMEText(corpo, 'plain'))

    # Connessione al server SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(mittente, password)

    # Invio dell'email
    testo_email = msg.as_string()
    server.sendmail(mittente, destinatario, testo_email)

    # Chiusura della connessione
    server.quit()

# Recupera gli studenti dal database
studenti = recupera_studenti()

# Invia email personalizzate agli studenti
for nome, email in studenti:
    oggetto = 'Ciao {}!'.format(nome)
    corpo = 'Corpo dell\'email personalizzato per {}'.format(nome)
    invia_email(email, oggetto, corpo)
