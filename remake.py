# Package Here!
import os
import json
import pprint
import socket
import requests

if __name__ == "__main__":
    OS = os.name
    match OS:
        case "posix" : os.system("clear")
        case "nt" : os.system("cls")    

def GetAPI(n): #Function for get response from API
    print("="*37)
    ip_address = socket.gethostbyname(n)

    requset_url = f"https://geolocation-db.com/jsonp/{ip_address}"
    # requset_url = 'https://geolocation-db.com/jsonp/' + ip_address
    response = requests.get(requset_url)
    geolocation = response.content.decode()
    geolocation = geolocation.split("(")[1].strip(")")
    geolocation = json.loads(geolocation)

    for i,o in geolocation.items():
        pprint.pprint(str(i) + ' : ' + str(o))



while True:
    fist_line = f"===== Get some information here ====="
    print(fist_line)
    print("")
    hostName = input('Enter domain name: ')

    # Call function here!
    GetAPI(hostName)

    # Conditional
    print("="*35)
    print("")
    isLanjut = str(input("Lanjut (y/n): "))
    if isLanjut == 'n' or isLanjut == 'N':
        break

    elif isLanjut == 'y' or isLanjut == 'Y':
        print("\n")
        continue

    else:
        print("--Command Failed--")
        break