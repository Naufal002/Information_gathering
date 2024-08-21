import os
import socket
import requests
import pprint

def get_geolocation(ip_address):
    request_url = f"http://ip-api.com/json/{ip_address}"
    retries = 3
    for attempt in range(retries):
        try:
            response = requests.get(request_url, timeout=10)  # Timeout 10 detik
            return response.json()  # Mengembalikan respons JSON langsung
        except requests.exceptions.ConnectTimeout:
            print(f"Connection timed out. Retrying... ({attempt+1}/{retries})")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            break
    return None

if __name__ == "__main__":
    OperatingSystem = os.name

    match OperatingSystem:
        case 'posix':
            os.system('clear')
        case 'nt':
            os.system('cls')

    #========================================
    hostName = input('Enter domain name: ')
    print("="*15)
    
    try:
        ip_address = socket.gethostbyname(hostName)
        print(f"IP Address: {ip_address}")
        print("="*15)
        
        geolocation = get_geolocation(ip_address)
        
        if geolocation:
            for key, value in geolocation.items():
                pprint.pprint(f"{key} : {value}")
        else:
            print("Failed to retrieve geolocation data.")
    except socket.gaierror:
        print("Invalid domain name.")