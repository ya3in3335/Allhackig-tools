import os
import shutil
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# قائمة الأدوات المطلوبة
TOOLS = {
    "nmap": "nmap",
    "nikto": "nikto",
    "sqlmap": "sqlmap",
    "hydra": "hydra",
    "metasploit-framework": "msfconsole",
    "gobuster": "gobuster",
    "john": "john",
    "theharvester": "theHarvester",
    "exploitdb": "searchsploit"
}

# فحص الأدوات وتثبيتها إذا لم تكن موجودة
def check_and_install_tools():
    missing_tools = [tool for tool, cmd in TOOLS.items() if not shutil.which(cmd)]
    
    if missing_tools:
        print(Fore.YELLOW + "\n[+] Installing missing tools...")
        os.system(f"sudo apt update && sudo apt install -y {' '.join(missing_tools)}")
        print(Fore.GREEN + "\n[+] All tools are installed successfully!")
    else:
        print(Fore.CYAN + "\n[+] All required tools are already installed.")

# مسح الشاشة وعرض الواجهة الحماسية
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(Fore.RED + """
██╗    ██╗ ██████╗ ██████╗ ███╗   ███╗    ███╗   ███╗███████╗███╗   ██╗
██║    ██║██╔═══██╗██╔══██╗████╗ ████║    ████╗ ████║██╔════╝████╗  ██║
██║ █╗ ██║██║   ██║██████╔╝██╔████╔██║    ██╔████╔██║█████╗  ██╔██╗ ██║
██║███╗██║██║   ██║██╔═══╝ ██║╚██╔╝██║    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║
╚███╔███╔╝╚██████╔╝██║     ██║ ╚═╝ ██║    ██║ ╚═╝ ██║███████╗██║ ╚████║
 ╚══╝╚══╝  ╚═════╝ ╚═╝     ╚═╝     ╚═╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝
""" + Fore.CYAN + """
    █████╗ ██╗     ██╗      ██╗  ██╗ █████╗  ██████╗██╗  ██╗
   ██╔══██╗██║     ██║      ██║  ██║██╔══██╗██╔════╝██║  ██║
   ███████║██║     ██║█████╗███████║███████║██║     ███████║
   ██╔══██║██║     ██║╚════╝██╔══██║██╔══██║██║     ██╔══██║
   ██║  ██║███████╗███████╗ ██║  ██║██║  ██║╚██████╗██║  ██║
   ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
""" + Fore.YELLOW + """
-------------------------------------------------------
🔥 Welcome to AllHacking-Tool by ya ya la 19 🔥
Made by Yacine
-------------------------------------------------------
""")

# قائمة الأدوات مع وظائفها الحقيقية
def run_tool(tool_name, command):
    clear_screen()
    print(Fore.GREEN + f"\n[+] Running {tool_name}...\n")
    os.system(command)

def main_menu():
    check_and_install_tools()  # تثبيت الأدوات إذا كانت ناقصة

    while True:
        clear_screen()
        banner()
        print(Fore.MAGENTA + """
        [1] Nmap - Network Scanner
        [2] Nikto - Web Vulnerability Scanner
        [3] SQLmap - Database Exploitation
        [4] Hydra - Brute Force Tool
        [5] Metasploit - Exploitation Framework
        [6] Gobuster - Directory and File Enumeration
        [7] John the Ripper - Password Cracking
        [8] TheHarvester - Information Gathering
        [9] ExploitDB - Search for Exploits
        [0] Exit
        """)

        choice = input(Fore.CYAN + "Select an option: ")

        if choice == "1":
            target = input(Fore.YELLOW + "Enter target (IP or domain): ")
            run_tool("Nmap", f"nmap -A {target}")
        elif choice == "2":
            target = input(Fore.YELLOW + "Enter target URL: ")
            run_tool("Nikto", f"nikto -h {target}")
        elif choice == "3":
            target = input(Fore.YELLOW + "Enter vulnerable URL: ")
            run_tool("SQLmap", f"sqlmap -u {target} --dbs")
        elif choice == "4":
            ip = input(Fore.YELLOW + "Enter target IP: ")
            userlist = input("Enter path to username list: ")
            passlist = input("Enter path to password list: ")
            run_tool("Hydra", f"hydra -L {userlist} -P {passlist} {ip} ssh")
        elif choice == "5":
            run_tool("Metasploit", "msfconsole")
        elif choice == "6":
            target = input(Fore.YELLOW + "Enter target URL: ")
            wordlist = input("Enter path to wordlist: ")
            run_tool("Gobuster", f"gobuster dir -u {target} -w {wordlist}")
        elif choice == "7":
            hashfile = input(Fore.YELLOW + "Enter path to hash file: ")
            run_tool("John the Ripper", f"john {hashfile}")
        elif choice == "8":
            domain = input(Fore.YELLOW + "Enter target domain: ")
            run_tool("TheHarvester", f"theHarvester -d {domain} -l 500 -b all")
        elif choice == "9":
            search = input(Fore.YELLOW + "Enter search term: ")
            run_tool("ExploitDB", f"searchsploit {search}")
        elif choice == "0":
            print(Fore.RED + "Exiting... Stay Safe!")
            break
        else:
            print(Fore.RED + "Invalid option! Try again.")

        input(Fore.BLUE + "\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
