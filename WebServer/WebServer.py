# Python Code for the Web Server
# import socket module 
from socket import * 
import sys  # In order to terminate the program 

serverSocket = socket(AF_INET, SOCK_STREAM) 

# Prepare a server socket 
# Fill in start
serverPort = 8080  # Porta su cui il server ascolta
serverSocket.bind(('', serverPort))  # Collega il socket a tutte le interfacce sulla porta specificata
serverSocket.listen(1)  # Il server è pronto a ricevere una connessione alla volta
# Fill in end

while True: 
    # Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()  # Fill in start (Accetta una connessione) # Fill in end
    
    try: 
        message = connectionSocket.recv(1024).decode()  # Fill in start (Riceve il messaggio) # Fill in end
        
        # Fill in start (Estrae il nome del file richiesto)              
        filename = message.split()[1]                  
        f = open(filename[1:])                         
        # Fill in end           
        
        # Fill in start (Legge il contenuto del file)          
        outputdata = f.read()       
        # Fill in end                    
        
        # Send one HTTP header line into socket 
        # Fill in start (Invia l'intestazione HTTP)
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        # Fill in end                 
        
        # Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):            
            connectionSocket.send(outputdata[i].encode()) 
        
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close() 
    
    except IOError: 
        # Send response message for file not found 
        # Fill in start 
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        # Fill in end 
        
        # Close client socket 
        # Fill in start 
        connectionSocket.close()
        # Fill in end             

# Termina il server
serverSocket.close() 
sys.exit()  
# Termina il programma dopo aver inviato i dati