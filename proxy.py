import socket, sys
from thread import *


def start():

	max_conn = 5
	buffer_size = 8192
	listening_port = 8181
	# try:
	# 	listening_port = int(raw_input("[*] Enter listening port number") )
	# except KeyboardInterrupt:
	# 	print "\n[*] User Requested an interrupt"
	# 	print "[*] Application Exiting ..."
	# 	sys.exit()


	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(('',listening_port))
		s.listen(max_conn)
		print "[*] Initializing Sockets ... Done"
		print "[*] Socket Binded Succesfully"
		print ("[*] Server started successfully  [%d]\n " % (listening_port) )
	except Exception, e:
		print "[*] Unable to initialize socket"
		print e
		sys.exit(2)


	while 1:
		try:
			print "rec"
			conn, addr = s.accept()
			data = conn.recv(buffer_size)
			start_new_thread(conn_string,(conn,data,addr))
		except KeyboardInterrupt, e:
			print e
			s.close()
			print "\n[*] Proxy Server shutting down ..."
			print "[*] Have a nice day ... "
			sys.exit(1)

	s.close()
		

def conn_string(conn,data,addr):
	print "amzmzmzmzmzm"
	try:


		first_line = data.split('\n')[0]
		url = first_line.split(' ')[1]

		print first_line
		
		http_pos = url.find("://")
		if (http_pos == -1):
			temp = url
		else:
			temp = url[(http_pos+3):]

		port_pos = temp.find(":")

		webserver_pos = temp.find("/")
		if webserver_pos == -1:
			webserver_pos = len(temp)

		webserver = ""
		port = -1
		if (port_pos == -1 or webserver_pos < port_pos):
			port = 80
			webserver = temp[:webserver_pos]
		else:
			port = int((temp[(port_pos+1):])[:webserver_pos - port_pos -1])
			webserver = temp[:port_pos]

		proxy_server(webserver,port,conn,data,addr)
	except Exception, e:
		print e


def proxy_server(webserver,port,conn,data,addr):
	try:
		print "aaaa",webserver,conn
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((webserver,port))
		s.send(data)

		buffer_size = 8192
		while 1:
			reply = s.recv(buffer_size)
			print "rpl"
			if (len(reply) > 0):
				conn.send(reply)
				dar = float(len(reply))
				dar = float(dar/1024)
				dar = "%.3s" % (str(dar))
				dar = "%s KB" %(dar)
				'pring a custom message for request complete'
				print "[*] Request done : %s => %s <=" %(str(addr[0]),str(dar))
			
			else:
				break

		s.close()
		conn.close()
	except socket.error, (value, message) :
		print  socket.error
		s.close()
		conn.close()
		sys.exit(1)
		


start()







