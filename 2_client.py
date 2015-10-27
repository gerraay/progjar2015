import sys
import socket
import select
import time
import string

host = 'localhost'
port = 8080
 
def client():
     
    # membuat TCP/IP socket
	x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
    # terhubung dengan remote host
	try :
		x.connect((host, port))
	except :
		print 'Klien gagal terhubung'
		sys.exit()
     
	print 'Klien sudah terhubung dengan remote host. Anda dapat mulai berkirim pesan.'
	sys.stdout.write('## '); sys.stdout.flush()
     
	while True:
		socket_list = [sys.stdin, x]
		 
		# Get the list sockets which are readable
		ready_to_read,ready_to_write,in_error = select.select(socket_list, [], [])
		 
		for sock in ready_to_read:      
		
			if sock == x:
				# incoming message from remote server, x
				data = sock.recv(4096)
				if not data :
					print '\nAnda terputus dari chat server.'
					sys.exit()
				else :
					sys.stdout.write(data)
					sys.stdout.write('## '); sys.stdout.flush()     
			
			else :
				# user memasukkan pesan
				msg = []
				temp = sys.stdin.readline()
				temp1 = string.split(temp[:-1])
				
				d=len(temp1)
				if temp1[0]=="login" :
					if d>2:
						print('Username cacat')
					elif d<2:
						print('Login butuh username')
					else:
						x.send(temp)
				
				elif temp1[0]=="list" :
					if d>1:
						print('Perintah List salah')
					else:
						x.send(temp)

<<<<<<< HEAD
				elif temp1[0]=="send" :
=======
				elif temp1[0]=="sendto" :
>>>>>>> 6e1e4e02399e89eb041a067dcf269241297b375e
					if d<3:
						print('Perintah Send salah')
					else:
						x.send(temp)
						
				elif temp1[0]=="sendall" :
					if d<2:
						print("Perintah SendAll salah")
					else:
						x.send(temp)
						
				else:
					print ('Perintah salah')

				sys.stdout.write('## '); sys.stdout.flush() 

<<<<<<< HEAD
client()
=======
client()
>>>>>>> 6e1e4e02399e89eb041a067dcf269241297b375e
