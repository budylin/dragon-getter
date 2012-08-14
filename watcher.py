import socket
import numpy
import struct
import pylab
import ctypes

HOST = 'localhost'    # The remote host
PORT = 13131 # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
comment = s.recv(4)
comment = struct.unpack('I', comment)[0]
if comment == 0:
    label = 'correlation'
elif comment == 1:
    label = 'chebyshev'
print comment
length = s.recv(4)
length = struct.unpack('I', length)[0]
print "length is {}".format(length)
datalen = length * 2 * ctypes.sizeof(ctypes.c_double)
data  = ''
print "datalen is {}".format(datalen)
while len(data) < datalen:
    data += s.recv(datalen - len(data))
    print "current len(data) = {}".format(len(data))
arr  = numpy.fromstring(data, dtype=float)
s.close()
pylab.title(label)
pylab.plot(arr[:length], '-')
pylab.plot(arr[length:], '-')
pylab.show()
