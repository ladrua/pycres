import socket   #for sockets
import sys  #for exit
from phue import Bridge
b = Bridge('192.168.10.16')
b.connect()
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
 
host = '192.168.10.10'
port = 50000
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip
 
#Send some data to remote s 
toit = 'I am a computer, I will send data to you.' # some binary data
s.send(toit)
noe = '000'

print 'Hello.'

reply = s.recv(4096)
while (noe != 'EXIT'):
    while (reply == 'L2=ON'):
        b.set_light(2,'on', True)
        b.set_light(3,'on', True)
        s.send('Light 2 is ON')
        print 'Light 2 and 3 is ON' 
        reply = s.recv(4096)
    while (reply == 'L2=OFF'):
        b.set_light(2,'on', False)
        b.set_light(3,'on', False)
        s.send('Light 2 is OFF')
        print 'Light 2 and 3 is OFF'    
        reply = s.recv(4096) 
    
    
print 'Goodbye!'
