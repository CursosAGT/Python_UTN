from Estructura import *
nuevo(0,"inicio");

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                      Socket                                 ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║   The primary socket API functions and methods in this module are:          ║
║                                                                             ║
║       socket()                                                              ║
║       bind()                                                                ║
║       listen()                                                              ║
║       accept()                                                              ║
║       connect()                                                             ║
║       connect_ex()                                                          ║
║       send()                                                                ║
║       recv()                                                                ║
║       close()                                                               ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
https://docs.python.org/2/library/socket.html


exception socket.error

    This exception is raised for socket-related errors. The accompanying value is either a string telling what went wrong or a pair (errno, string) representing an error returned by a system call, similar to the value accompanying os.error. See the module errno, which contains names for the error codes defined by the underlying operating system.

    Changed in version 2.6: socket.error is now a child class of IOError.

exception socket.herror

    This exception is raised for address-related errors, i.e. for functions that use h_errno in the C API, including gethostbyname_ex() and gethostbyaddr().

    The accompanying value is a pair (h_errno, string) representing an error returned by a library call. string represents the description of h_errno, as returned by the hstrerror() C function.

exception socket.gaierror

    This exception is raised for address-related errors, for getaddrinfo() and getnameinfo(). The accompanying value is a pair (error, string) representing an error returned by a library call. string represents the description of error, as returned by the gai_strerror() C function. The error value will match one of the EAI_* constants defined in this module.

exception socket.timeout

    This exception is 
""")
import socket 
import sys  





nuevo(0,"inicio");
#################################################################
host_ip = socket.gethostbyname('www.google.com')
print (host_ip)


#################################################################
nuevo(1);
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ("Socket successfully created")
except socket.error as err: 
    print ("socket creation failed with error %s" %(err) )
  
# default port for socket 
port = 80
  
try: 
    host_ip = socket.gethostbyname('www.google.com') 
except socket.gaierror: 
  
    # this means could not resolve the host 
    print ("there was an error resolving the host")
    sys.exit() 
  
# connecting to the server 
s.connect((host_ip, port)) 
  
print ("the socket has successfully connected to google on port == %s" %(host_ip) )

#################################################################
nuevo(2);

# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
  
# receive data from the server 
print (s.recv(1024)) 
# close the connection 
s.close()  

#################################################################
nuevo(3);
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
def fin():
	s = socket.socket()   
	s.bind(("localhost", 8000))  
	s.listen(1)  
	  
	sc, addr = s.accept()  
	  
	while True:  
		recibido = sc.recv(1024)  
		if recibido == "quit":  
		 break        
		print ("Recibido:", recibido)  
		sc.send(recibido)  
	  
	print ("adios")
	  
	sc.close()  
	s.close()  
