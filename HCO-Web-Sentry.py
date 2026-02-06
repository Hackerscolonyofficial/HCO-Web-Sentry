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

def print_banner():
    # Large ASCII Art Banner
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
    """Installs Nikto and ensures it is ready for direct execution."""
    print(f"{YELLOW}[*] Checking for Nikto engine...{RESET}")
    if shutil.which("perl") is None:
        os.system("pkg install perl git -y")
    if not os.path.exists(NIKTO_PATH):
        os.system(f"git clone https://github.com/sullo/nikto {HOME}/nikto")
        os.system(f"chmod +x {NIKTO_PATH}")
    print(f"{GREEN}[+] Engine verified at: {NIKTO_PATH}{RESET}")
    time.sleep(1)

def redirect_to_youtube():
    os.system('clear')
    print(f"{RED}{BOLD}[!] TOOL IS LOCKED!{RESET}")
    print(f"{YELLOW}To use this tool, subscribe and click the bell icon...{RESET}")
    for i in range(9, 0, -1):
        print(f"{RED}{i}...{RESET}", end=" ", flush=True)
        time.sleep(1)
    print("\n\033[94m[*] Redirecting to YouTube App...\033[0m")
    time.sleep(1)
    channel_url = "https://youtube.com/@hackers_colony_tech?si=fEyQbmfEOGMl_3Xn"
    os.system(f"termux-open {channel_url}")
    input(f"\n{GREEN}[+] Once subscribed, hit ENTER to unlock 🔓{RESET}")

def main_dashboard():
    os.system('clear')
    print_banner()
    
    # Red Box Sub-Header
    print(f"{BG_RED}{' '*52}{RESET}")
    print(f"{BG_RED}{BOLD}{GREEN}       HCO WEBSITE VULNERABILITY FINDER           {RESET}{BG_RED}  {RESET}")
    print(f"{BG_RED}{' '*52}{RESET}")
    
    print(f"\n{BLUE}[1]{RESET} Full Site Audit (Vulnerability Scan)")
    print(f"{BLUE}[2]{RESET} Check for Outdated Server Software")
    print(f"{BLUE}[3]{RESET} Scan for Hidden Directories")
    print(f"{BLUE}[4]{RESET} Exit")
    
    choice = input(f"\n{YELLOW}[?] Select an option: {RESET}")
    
    if choice == '1':
        target = input(f"{BLUE}[*] Enter Website URL (e.g., example.com): {RESET}")
        print(f"{GREEN}[*] Initializing deep scan on {target}...{RESET}")
        if os.path.exists(NIKTO_PATH):
            os.system(f"perl {NIKTO_PATH} -h {target}")
        else:
            print(f"{RED}[!] Error: Nikto file missing!{RESET}")
        input(f"\n{YELLOW}Scan finished. Press Enter to return.{RESET}")
        main_dashboard()
    elif choice == '4':
        print(f"{GREEN}Thanks for using HCO-Web-Sentry!{RESET}")
        sys.exit()
    else:
        print(f"{RED}[!] Invalid choice or module under update.{RESET}")
        time.sleep(2)
        main_dashboard()

if __name__ == "__main__":
    redirect_to_youtube()
    fix_engine()
    main_dashboard()
