import telnetlib
import numpy

HOST="192.168.43.161"
t=telnetlib.Telnet(HOST)
print t.read_all()
##t.read_until("mininet-vm login:")
#print t.read_all()
#t.read_eager()
#print t.read_all()
t.write("mininet\n\r")
print t.read_all()
t.read_until("Password:")
print t.read_all()
t.write("mininet\n\r")
print t.read_all()
t.read_until("mininet@mininet-vm:~$")
print t.read_all()
t.write("ls -ltr\r")
print t.read_all()
t.read_until("mininet@mininet-vm:~$")
print t.read_all()
t.write("exit\r")
print t.read_all()

