#script du client et de son application utilisant tkinter
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # possibilité que le client est quitter le serveur
            break


def send(event=None):  # envoie du message
    msg = client_msg.get()
    client_msg.set("")
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{leave}": # option pour quitter l'application
        client_socket.close()
        top.quit()


def on_closing(event=None):
    client_msg.set("{leave}")
    send()

top = tkinter.Tk()
top.title("WhatsPyApp")

#app tkinter
messages_frame = tkinter.Frame(top)
client_msg = tkinter.StringVar()  # Frame d'envoie du message
client_msg.set("message ici!")
scrollbar = tkinter.Scrollbar(messages_frame)  # barre de navigation dans l'historique des messages
# frame contenant l'historique des messages
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=client_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="envoie", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

# Entrée de l'ip du serveur et du port (3300) 
HOST = input('host: ')
PORT = input('port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # lancement de l'app