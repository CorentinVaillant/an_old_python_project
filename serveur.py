#script du serveur
from socket import AF_INET, socket, SOCK_STREAM, socket, gethostname, socket, gethostbyname
from threading import Thread

serveur_name= gethostname()
ip_address = gethostbyname(serveur_name)


#Gestion des différents utilisateurs connecter
def acceptIncomingConnections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s connected." % client_address)
        client.send(bytes("Connected!", "utf8"))
        client.send(bytes("Tapez votre nom", "utf8"))
        addresses[client] = client_address
        Thread(target=handleClient, args=(client,)).start()

#Gestion d'un utilisateur connecter
def handleClient(client):  # Prend le socket client comme paramètre.

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = "Bienvenu %s! Pour quitter l'app tapez : {leave} ." % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{leave}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{leave}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s n'est plus avec nous." % name, "utf8"))
            break


#envoi un message à tout les utilisateurs connecter
def broadcast(msg, prefix=""):  # la variable prefix est pour l'identification entre les utilisateurs

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print(
        f"Serveur name : {serveur_name} \n Ip address : {ip_address} \n \n Waiting for connection... \n")
    ACCEPT_THREAD = Thread(target=acceptIncomingConnections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()

#fin du script