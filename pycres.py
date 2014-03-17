import socket   #for sockets
import sys  #for exit
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

print 'Socket Created'

host = '192.168.10.10' #Your Crestron Processor IP here.
port = 5005 #The port you specified in you Simpl programs TCP/IP Server symbol.

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

print 'Welcome.'

reply = s.recv(4096)
while (reply != 'EXIT'):
    print reply
    s.send('You just told me: "%s"' % reply)
    s.send('Tell me something... or send "EXIT" to end me.')
    reply = s.recv(4096)
print 'Goodbye!'
