import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
#url = 'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'
mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    
    data = mysock.recv(64)
    if ( len(data) < 1 ) : break
    x = data.decode('utf8')
    print (x)
    mysock.close()
      



