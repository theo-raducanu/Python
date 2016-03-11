'''
    udp socket client
    Silver Moon
'''
 
import socket   #for sockets
import sys  #for exit
 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
host = 'localhost';
port = 1009;
 
msg = raw_input('Enter message to send : ')

while(msg) :
    
    s.settimeout(2)
    acknowledged = False
    while not acknowledged: 
        try :
            #Set the whole string
            s.sendto(msg, (host, port))
            
            # receive data from client (data, addr)
            d = s.recvfrom(1024)
            reply = d[0]
            addr = d[1]
            acknowledged = True

        except socket.timeout:
            print "Timeout reached, re-sending"
            s.sendto(msg, (host, port))
        print 'Server reply : ' + reply 
    msg = raw_input('Enter message to send : ')
   #except socket.error, msg:
       #print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
       #sys.exit()