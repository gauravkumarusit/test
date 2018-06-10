import getpass
import sys
import telnetlib

HOST = "192.168.43.161"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls -ltr\n")

#print tn.read_eager()
tn.write("sudo bash\n")
tn.read_until("#")
tn.write("vtysh\n")
tn.read_until("#")
tn.write("exit\n")

print tn.read_all()