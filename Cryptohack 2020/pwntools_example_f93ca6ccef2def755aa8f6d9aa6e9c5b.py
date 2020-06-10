import telnetlib
import json
import codecs
from Crypto.Util.number import long_to_bytes

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

for i in range(101):
	received = json_recv()
	print(received)

	print("Received type: ")
	print(received["type"])
	print("Received encoded value: ")
	print(received["encoded"])

	if(received['type']=='base64'):
		ans = codecs.decode(received['encoded'].encode(),'base64').decode()
	elif(received['type']=='hex'):
		ans = codecs.decode(received['encoded'],'hex').decode()
	elif(received['type']=='utf-8'):
		ans = ''.join([chr(j) for j in received['encoded']])
	elif(received['type']=='rot13'):
		ans = codecs.decode(received['encoded'],'rot-13')
	elif(received['type']=='bigint'):
		ans = long_to_bytes(int(received['encoded'],16)).decode()

	to_send = {
	    "decoded": ans
	}
	json_send(to_send)