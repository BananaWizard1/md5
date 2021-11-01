import socket as soc
import hashlib
import threading
import webbrowser

msg = ""

def listen(soc):
    global msg
    msg = soc.recv(1024).decode().split(",")[0]

client_socket = soc.socket()
client_socket.connect(("127.0.0.1",13370))
client_socket.send("howdy".encode())
my_id = int(client_socket.recv(1024).decode())
client_socket.close()
abc = 'abcdefghijklmnopqrstvwxyz'
found = False
serv_soc = soc.socket()
serv_soc.bind(("127.0.0.1",13370 + my_id))
serv_soc.listen(5)
boss_soc, boss_addr = serv_soc.accept()
task = boss_soc.recv(1024).decode()
start = task.split(",")[0]
stop = task.split(",")[1]
md5 = task.split(",")[2]
x = threading.Thread(target=listen, args=(boss_soc,))
x.start()
p = -1
print("searching..")
while (not found) and (msg == "") and (start != stop):
    while(start[p]>'z'):
        start = list(start)
        start[p] = 'a'
        start = "".join(start)
        p = p - 1
        start = start[:p] + chr(ord(start[p]) + 1)
        while(len(start) != len(stop)):
            start = start + 'a'
    p = -1
    hash_object = hashlib.md5(start.encode())
    pw = hash_object.hexdigest()
    if (pw == md5):
        found = True
        break
    elif (pw == stop):
        break    
    if(not found):
        pw = ""
    start=start[:p]+chr(ord(start[p])+1)
if (msg != "" or found):
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
elif (not found):
    hash_object = hashlib.md5(start.encode())
    pw = hash_object.hexdigest()
    if (pw == md5):
        found = True
pw = start
final_rep = ""
if (found):
    final_rep = str(my_id) + ",True," + md5 + "," + pw#לשנות pw
elif (not found):
    final_rep = str(my_id) + ",False," + md5
if(msg == ""):
    boss_soc.send(final_rep.encode())
i=input("end")
    


