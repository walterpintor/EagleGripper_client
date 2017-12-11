import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.56.1', 5004)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

# Variables
Gain = "5"
Kp = "9"
Ki = "17"
Kd = "10"

velocity = 0
current = 400

try:
    
    # Send data
    message = 'startCommClient'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while 1:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'Received: "%s"' % data
        print amount_received
        print amount_expected
        time.sleep( 2 )
	if (data == "startServer"):
	    data = sock.recv(16)
            amount_received += len(data)
            print >>sys.stderr, 'Received: "%s"' % data
            time.sleep( 1 )

	if (data == "getPIDvalues"):
	    sock.sendall('Roger')
		
	    sock.sendall(Gain)
	    time.sleep( 1 )
	    sock.sendall(Kp)
	    time.sleep( 1 )
	    sock.sendall(Ki)
	    time.sleep( 1 )
	    sock.sendall(Kd)
	    
	    data = "0"


	if (data == "setPIDvalues"):
	    
            value1 = sock.recv(24)
	    print value1

	    index = value1.find('$')
	    value1.split('$')
            information = value1.split('$')
	    indexes = value1.index('$')
            Gain = information[0]	    
            print >>sys.stderr, 'Received Gain: "%s"' % Gain

            Kp = information[1]
            print >>sys.stderr, 'Received Kp: "%s"' % Kp
              
            Ki = information[2]
            print >>sys.stderr, 'Received Ki: "%s"' % Ki

            Kd = information[3]
            print >>sys.stderr, 'Received Kd: "%s"' % Kd
	
	    sock.sendall('startCommClient')
            data = "0"

	##Defining rotation speed##
	if (data == "rotateCMD"):
	   
	   velocity = sock.recv(12)
	   print >>sys.stderr, 'Velocity commanded (RPMs): "%s"' % velocity

           sock.sendall('startCommClient')
	   data = "0"

	##Setting limit of current##
	if (data == "currentLimit"):

	   current = sock.recv(12)
	   print >>sys.stderr, 'Current limit (mA): "%s"' % current

	   sock.sendall('startCommClient')
	   data = "0"


finally:
    print >>sys.stderr, 'closing socket'
    sock.close()





    
