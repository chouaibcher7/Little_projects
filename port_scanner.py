import socket

target=str(input('IP address : '))
ports=[19,20,21,22,23,24,25,80,443]
for p in ports:
                           #ipV4               #TCP
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    r=s.connect_ex((target,p))
    if r==0:
        service=socket.getservbyport(p)
        print('the port {}:{} is open'.format(p,service))
#coded by chou@ibcher+
