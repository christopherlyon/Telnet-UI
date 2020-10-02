import getpass
import telnetlib

HOST = "10.165.178.140"
user = "root"
password = "rootroot"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"cli video Off\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
