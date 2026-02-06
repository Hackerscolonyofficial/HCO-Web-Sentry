import os
import sys
import time
import subprocess
import threading

# --- COLORS & STYLES ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"
BG_RED = "\033[41m"

def redirect_to_youtube():
    os.system('clear')
    print(f"{RED}{BOLD}[!] TOOL IS LOCKED!{RESET}")
    print(f"{YELLOW}To use this tool, subscribe and click the bell icon...{RESET}")
    
    # Countdown
    for i in range(9, 0, -1):
        print(f"{RED}{i}...{RESET}", end=" ", flush=True)
        time.sleep(1)
    
    print("\n\033[94m[*] Redirecting to YouTube App...\033[0m")
    time.sleep(1)
    
    # Redirect command for Termux (using termux-open)
    channel_url = "https://youtube.com/@hackers_colony_tech?si=fEyQbmfEOGMl_3Xn"
    os.system(f"termux-open {channel_url}")
    
    # Wait for user to return
    input(f"\n{GREEN}[+] Once subscribed, hit ENTER to unlock 🔓{RESET}")

def main_dashboard():
    os.system('clear')
    # Drawing the Red Box with Bold Green Text
    print(f"{BG_RED}{BOLD}{' '*45}{RESET}")
    print(f"{BG_RED}{BOLD}  {GREEN}HCO WEBSITE VULNERABILITY FINDER           {RESET}{BG_RED}  {RESET}")
    print(f"{BG_RED}{BOLD}{' '*45}{RESET}")
    
    print(f"\n{BLUE}[1]{RESET} Full Site Audit (Nikto Engine)")
    print(f"{BLUE}[2]{RESET} SQL Injection Heuristic Check")
    print(f"{BLUE}[3]{RESET} XSS Vulnerability Scanner")
    print(f"{BLUE}[4]{RESET} Directory Brute-Forcer")
    print(f"{BLUE}[5]{RESET} Exit")
    
    choice = input(f"\n{YELLOW}[?] Select an option: {RESET}")
    handle_choice(choice)

def handle_choice(choice):
    if choice == '1':
        target = input(f"{BLUE}[*] Enter Website URL: {RESET}")
        print(f"{GREEN}[*] Initializing deep scan on {target}...{RESET}")
        # Command to run Nikto (assumes nikto is installed via setup.sh)
        os.system(f"nikto -h {target}")
    elif choice == '5':
        sys.exit()
    else:
        print(f"{RED}[!] Feature under development for next update.{RESET}")
        time.sleep(2)
        main_dashboard()

if __name__ == "__main__":
    redirect_to_youtube()
    main_dashboard()
