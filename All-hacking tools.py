import os
import time

# مسح الشاشة وعرض الواجهة الحماسية
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
    █████╗ ██╗     ██╗      ██╗  ██╗ █████╗  ██████╗██╗  ██╗
   ██╔══██╗██║     ██║      ██║  ██║██╔══██╗██╔════╝██║  ██║
   ███████║██║     ██║█████╗███████║███████║██║     ███████║
   ██╔══██║██║     ██║╚════╝██╔══██║██╔══██║██║     ██╔══██║
   ██║  ██║███████╗███████╗ ██║  ██║██║  ██║╚██████╗██║  ██║
   ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    -------------------------------------------------------
    🔥 Welcome to AllHacking-Tool by ya ya la 19 🔥
    -------------------------------------------------------
    """)

def nmap_menu():
    clear_screen()
    print("\n[+] Nmap - Network Scanner\n")
    target = input("Enter target (IP or domain): ")
    print("""
    [1] Basic scan: nmap <target>
    [2] OS and version detection: nmap -A <target>
    [3] Aggressive scan: nmap -T4 -A -v <target>
    [4] Scan all ports: nmap -p- <target>
    [5] Scan for vulnerabilities: nmap --script vuln <target>
    """)
    choice = input("Select an option: ")
    commands = {
        "1": f"nmap {target}",
        "2": f"nmap -A {target}",
        "3": f"nmap -T4 -A -v {target}",
        "4": f"nmap -p- {target}",
        "5": f"nmap --script vuln {target}"
    }
    os.system(commands.get(choice, "echo Invalid choice!"))

def nikto_menu():
    clear_screen()
    print("\n[+] Nikto - Web Vulnerability Scanner\n")
    target = input("Enter target URL: ")
    print("""
    [1] Basic scan: nikto -h <target>
    [2] Scan with SSL: nikto -h <target> -ssl
    [3] Scan with user agent: nikto -h <target> -useragent Mozilla
    [4] Save output: nikto -h <target> -output result.txt
    """)
    choice = input("Select an option: ")
    commands = {
        "1": f"nikto -h {target}",
        "2": f"nikto -h {target} -ssl",
        "3": f"nikto -h {target} -useragent Mozilla",
        "4": f"nikto -h {target} -output result.txt"
    }
    os.system(commands.get(choice, "echo Invalid choice!"))

def sqlmap_menu():
    clear_screen()
    print("\n[+] SQLmap - Database Exploitation\n")
    target = input("Enter vulnerable URL: ")
    print("""
    [1] Detect DBMS: sqlmap -u <target> --dbs
    [2] Get tables: sqlmap -u <target> -D <database> --tables
    [3] Dump data: sqlmap -u <target> -D <database> -T <table> --dump
    """)
    choice = input("Select an option: ")
    if choice == "1":
        os.system(f"sqlmap -u {target} --dbs")
    elif choice == "2":
        db = input("Enter database name: ")
        os.system(f"sqlmap -u {target} -D {db} --tables")
    elif choice == "3":
        db = input("Enter database name: ")
        table = input("Enter table name: ")
        os.system(f"sqlmap -u {target} -D {db} -T {table} --dump")
    else:
        print("Invalid choice!")

def hydra_menu():
    clear_screen()
    print("\n[+] Hydra - Brute Force Tool\n")
    ip = input("Enter target IP: ")
    userlist = input("Enter path to username list: ")
    passlist = input("Enter path to password list: ")
    print("""
    [1] SSH Attack: hydra -L <userlist> -P <passlist> <ip> ssh
    [2] FTP Attack: hydra -L <userlist> -P <passlist> ftp://<ip>
    [3] HTTP Form Attack: hydra -L <userlist> -P <passlist> <ip> http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect"
    """)
    choice = input("Select an option: ")
    commands = {
        "1": f"hydra -L {userlist} -P {passlist} {ip} ssh",
        "2": f"hydra -L {userlist} -P {passlist} ftp://{ip}",
        "3": f'hydra -L {userlist} -P {passlist} {ip} http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect"'
    }
    os.system(commands.get(choice, "echo Invalid choice!"))

def metasploit_menu():
    clear_screen()
    print("\n[+] Metasploit - Exploitation Framework\n")
    print("""
    [1] Launch Metasploit: msfconsole
    [2] Search exploits: search <exploit>
    [3] Use exploit: use <exploit>
    """)
    choice = input("Select an option: ")
    if choice == "1":
        os.system("msfconsole")
    elif choice == "2":
        exploit = input("Enter exploit name: ")
        os.system(f"msfconsole -q -x 'search {exploit}; exit'")
    elif choice == "3":
        exploit = input("Enter exploit name: ")
        os.system(f"msfconsole -q -x 'use {exploit}; show options; exit'")
    else:
        print("Invalid choice!")

def main_menu():
    while True:
        clear_screen()
        banner()
        print("""
        [1] Nmap - Network Scanner
        [2] Nikto - Web Vulnerability Scanner
        [3] SQLmap - Database Exploitation
        [4] Hydra - Brute Force Tool
        [5] Metasploit - Exploitation Framework
        [0] Exit
        """)
        
        choice = input("Select an option: ")

        if choice == "1":
            nmap_menu()
        elif choice == "2":
            nikto_menu()
        elif choice == "3":
            sqlmap_menu()
        elif choice == "4":
            hydra_menu()
        elif choice == "5":
            metasploit_menu()
        elif choice == "0":
            print("Exiting... Stay Safe!")
            break
        else:
            print("Invalid option! Try again.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
