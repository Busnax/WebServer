# Web Server in Python

## Descrizione del Progetto

In questo progetto, ho sviluppato un semplice **web server** in Python come parte del laboratorio "Web Server Lab". Il server è in grado di gestire una richiesta HTTP alla volta, accettare e analizzare richieste HTTP GET, recuperare file richiesti dal file system del server e inviare la risposta HTTP al client. Se il file richiesto non è presente, il server risponde con un messaggio di errore **404 Not Found**.

### Funzionalità Implementate

- **Creazione del socket** per connessioni TCP.
- **Parsing delle richieste HTTP** per estrarre il file richiesto.
- **Gestione delle risposte HTTP**, incluse intestazioni e contenuto del file richiesto.
- **Gestione degli errori**: invio di un messaggio di errore 404 per file non trovati.
- **Supporto ai file HTML**: il server può servire file come `HelloWorld.html`.

### Come Avviare il Server

1. Posiziona un file HTML (ad esempio, `HelloWorld.html`) nella stessa directory dello script Python.
2. Avvia il server utilizzando il seguente comando:
   ```bash
   python3 WebServer.py
   ```
3. Determina l'indirizzo IP del tuo server e utilizza un browser per accedere al file:
   ```text
   http://<IP_del_server>:<porta>/HelloWorld.html
   ```
   Sostituisci `<IP_del_server>` con l'indirizzo IP del tuo host e `<porta>` con la porta configurata nel codice (ad esempio, `8080`).

4. Se richiedi un file non presente nel server, il browser mostrerà un messaggio di errore 404.

### Estensioni Opzionali

Sono stati forniti esercizi aggiuntivi per estendere il progetto:

1. **Server Multithreaded**: Un server in grado di gestire più richieste simultaneamente utilizzando threading.
2. **Client HTTP Personalizzato**: Uno script Python per testare il server, che invia richieste HTTP GET e visualizza le risposte.

### Tecnologie Utilizzate

- **Python**: per la gestione del server e delle connessioni socket.
- **Protocollo HTTP**: per la comunicazione client-server.
- **HTML**: per creare i file serviti dal server.
