import os

if __name__ == "__main__":
    OperatingSystem = os.name

    match OperatingSystem:
        case 'posix' : os.system('clear')
        case 'nt' : os.system('cls')

# Package Here!
import socket
import requests
import pprint
import json

hostName = input('Enter domain name: ')
print("="*15)
ip_address = socket.gethostbyname(hostName)

requset_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(requset_url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)

for i,o in geolocation.items():
    pprint.pprint(str(i) + ' : ' + str(o))