import os

if __name__ == "__main__":
    OperatingSystem = os.name

    match OperatingSystem:
        case 'posix' : os.system('clear')
        case 'nt' : os.system('cls')