import os
import shutil
import time
import colorama
from colorama import Fore, Style
from pyfiglet import Figlet

colorama.init(autoreset=True)

# الأدوات المطلوبة
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

# تحميل الأدوات
INSTALL_COMMAND = "sudo apt update && sudo apt install -y {}"

# شكل مجهر ASCII
MICROSCOPE = r'''
         _____
        /     \
       | () () |
        \  ^  /
         |||||
         |||||
     ____|||||____
    /    |||||    \
   /     |||||     \
  /      |||||      \
 /       |||||       \
/_____________________\
'''

# عرض نص ببطء كآلة كاتبة
def typewriter(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

# تنظيف الشاشة
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# تثبيت الأدوات
def install_tools():
    clear()
    print(Fore.YELLOW + "[+] Checking and Installing Tools...")
    missing = [pkg for pkg, cmd in TOOLS.items() if not shutil.which(cmd)]
    if missing:
        os.system(INSTALL_COMMAND.format(' '.join(missing)))
        print(Fore.GREEN + "[+] All tools installed successfully!")
    else:
        print(Fore.CYAN + "[+] All required tools are already installed!")
    time.sleep(2)

# الشعار الكبير
def big_banner():
    f = Figlet(font='slant')
    print(Fore.RED + f.renderText('ALL-SCANN'))
    print(Fore.LIGHTBLUE_EX + MICROSCOPE)
    print(Fore.CYAN + "Made by ⚡𝙏𝙞𝙢𝙤 | Telegram: https://t.me/hacker16_thsb\n")

# وصف الأداة
def description():
    clear()
    text = """
[+] ALL-SCANN is your all-in-one offensive security terminal tool.
[+] From scanning to exploitation, everything is integrated in one place.
[+] Trusted by hackers. Powered by open source.
    """
    typewriter(Fore.LIGHTGREEN_EX + text)
    time.sleep(2)

# تشغيل أداة
def run_tool(name, command):
    clear()
    print(Fore.GREEN + f"[+] Running {name}...\n")
    os.system(command)

# الواجهة الرئيسية
def main_menu():
    while True:
        clear()
        big_banner()
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
            target = input("Enter target (IP or domain): ")
            run_tool("Nmap", f"nmap -A {target}")
        elif choice == "2":
            target = input("Enter target URL: ")
            run_tool("Nikto", f"nikto -h {target}")
        elif choice == "3":
            target = input("Enter vulnerable URL: ")
            run_tool("SQLmap", f"sqlmap -u {target} --dbs")
        elif choice == "4":
            ip = input("Enter target IP: ")
            userlist = input("Enter path to username list: ")
            passlist = input("Enter path to password list: ")
            run_tool("Hydra", f"hydra -L {userlist} -P {passlist} {ip} ssh")
        elif choice == "5":
            run_tool("Metasploit", "msfconsole")
        elif choice == "6":
            target = input("Enter target URL: ")
            wordlist = input("Enter path to wordlist: ")
            run_tool("Gobuster", f"gobuster dir -u {target} -w {wordlist}")
        elif choice == "7":
            hashfile = input("Enter path to hash file: ")
            run_tool("John the Ripper", f"john {hashfile}")
        elif choice == "8":
            domain = input("Enter target domain: ")
            run_tool("TheHarvester", f"theHarvester -d {domain} -l 500 -b all")
        elif choice == "9":
            search = input("Enter search term: ")
            run_tool("ExploitDB", f"searchsploit {search}")
        elif choice == "0":
            print(Fore.RED + "Exiting... Stay safe!")
            break
        else:
            print(Fore.RED + "Invalid option! Try again.")

        input(Fore.BLUE + "\nPress Enter to continue...")

if __name__ == "__main__":
    install_tools()
    description()
    clear()
    main_menu()
