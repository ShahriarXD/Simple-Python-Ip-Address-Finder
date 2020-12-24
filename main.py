import socket
from requests import get

# A hostname is a label that is assigned to a device connected to a computer network 
# and that is used to identify the device in various forms of electronic communication.

#so we need to use (hostname) in order to determine the host

# https://www.ipify.org/
# https://www.my-ip.io/api
# or https://seeip.org/ 

hostname = socket.gethostname()
localip = socket.gethostbyname(hostname)
publicip = get("https://api.my-ip.io/ip").text

print(f"""Simple Python Ip Address Finder

Hostname : {hostname}
Local Ip : {localip}
Local Ip : {publicip}""")
