import os
import sys
import time
import subprocess
import shutil

# --- COLORS & STYLES ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"
BG_RED = "\033[41m"

# Path configuration for Termux
HOME = os.environ.get('HOME')
NIKTO_PATH = f"{HOME}/nikto/program/nikto.pl"
REPORT_DIR = f"{HOME}/HCO_Reports"

def print_banner():
    banner = f"""{GREEN}{BOLD}
 ██╗  ██╗ ██████╗  ██████╗ 
 ██║  ██║██╔════╝ ██╔═══██╗
 ███████║██║      ██║   ██║
 ██╔══██║██║      ██║   ██║
 ██║  ██║╚██████╗ ╚██████╔╝
 ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ 
 ██╗    ██╗███████╗██████╗ 
 ██║    ██║██╔════╝██╔══██╗
 ██║ █╗ ██║█████╗  ██████╔╝
 ██║███╗██║██╔══╝  ██╔══██╗
 ╚███╔███╔╝███████╗██████╔╝
  ╚══╝╚══╝ ╚══════╝╚═════╝ 
 ███████╗███████╗███╗   ██╗████████╗██████╗ ██╗   ██╗
 ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚██╗ ██╔╝
 ███████╗█████╗  ██╔██╗ ██║   ██║   ██████╔╝ ╚████╔╝ 
 ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗  ╚██╔╝  
 ███████║███████╗██║ ╚████║   ██║   ██║  ██║   ██║   
 ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   
{RESET}"""
    print(banner)

def fix_engine():
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)
    if shutil.which("perl") is None:
        os.system("pkg install perl git -y")
    if not os.path.exists(NIKTO_PATH):
        print(f"{YELLOW}[*] Downloading Real-World Scanning Engine...{RESET}")
        os.system(f"git clone https://github.com/sullo/nikto {HOME}/nikto")
        os.system(f"chmod +x {NIKTO_PATH}")

def redirect_to_youtube():
    os.system('clear')
    print(f"{RED}{BOLD}[!] TOOL IS LOCKED!{RESET}")
    print(f"{YELLOW}To use this tool, subscribe and click the bell icon...{RESET}")
    for i in range(9, 0, -1):
        print(f"{RED}{i}...{RESET}", end=" ", flush=True)
        time.sleep(1)
    os.system(f"termux-open https://youtube.com/@hackers_colony_tech?si=fEyQbmfEOGMl_3Xn")
    input(f"\n{GREEN}[+] Once subscribed, hit ENTER to unlock 🔓{RESET}")

def main_dashboard():
    os.system('clear')
    print_banner()
    print(f"{BG_RED}{' '*52}{RESET}")
    print(f"{BG_RED}{BOLD}{GREEN}       HCO WEBSITE VULNERABILITY FINDER           {RESET}{BG_RED}  {RESET}")
    print(f"{BG_RED}{' '*52}{RESET}")
    
    print(f"\n{BLUE}[1]{RESET} Full Site Audit (Vulnerability Scan)")
    print(f"{BLUE}[2]{RESET} Check for Outdated Server Software (Tuning b)")
    print(f"{BLUE}[3]{RESET} Scan for Hidden Directories (Mutate 1)")
    print(f"{BLUE}[4]{RESET} Exit")
    
    choice = input(f"\n{YELLOW}[?] Select an option: {RESET}")
    
    if choice in ['1', '2', '3']:
        target = input(f"{BLUE}[*] Enter Website URL (e.g., example.com): {RESET}")
        report_file = f"{REPORT_DIR}/{target.replace('.', '_')}_scan.txt"
        print(f"{GREEN}[*] Real-time scan started on {target}...{RESET}")
        print(f"{YELLOW}[*] Report will be saved to: {report_file}{RESET}\n")
        
        # Mapping choices to real Nikto commands
        if choice == '1':
            # Full scan + save to file
            os.system(f"perl {NIKTO_PATH} -h {target} -o {report_file}")
        elif choice == '2':
            # Software identification only + save to file
            os.system(f"perl {NIKTO_PATH} -h {target} -Tuning b -o {report_file}")
        elif choice == '3':
            # Bruteforce common directories + save to file
            os.system(f"perl {NIKTO_PATH} -h {target} -mutate 1 -Cgidirs all -o {report_file}")
            
        print(f"\n{GREEN}[+] Scan Complete! Check {report_file} for details.{RESET}")
        input(f"\n{YELLOW}Press Enter to return to Dashboard.{RESET}")
        main_dashboard()
        
    elif choice == '4':
        print(f"{GREEN}Exiting... Don't forget to like and subscribe!{RESET}")
        sys.exit()
    else:
        print(f"{RED}[!] Invalid choice.{RESET}")
        time.sleep(2)
        main_dashboard()

if __name__ == "__main__":
    redirect_to_youtube()
    fix_engine()
    main_dashboard()
