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

def fix_engine():
    """Automatically installs Nikto if not found in Termux."""
    if shutil.which("nikto") is None:
        print(f"{YELLOW}[*] Nikto engine not found. Fixing environment...{RESET}")
        try:
            os.system("pkg install perl git -y")
            # Clone to home directory to ensure it stays permanent
            home = os.environ.get('HOME')
            if not os.path.exists(f"{home}/nikto"):
                os.system(f"git clone https://github.com/sullo/nikto {home}/nikto")
            
            # Create symlink to make 'nikto' command global
            os.system(f"ln -s {home}/nikto/program/nikto.pl $PREFIX/bin/nikto")
            os.system("chmod +x $PREFIX/bin/nikto")
            print(f"{GREEN}[+] Engine fixed successfully!{RESET}")
            time.sleep(2)
        except Exception as e:
            print(f"{RED}[!] Auto-fix failed: {e}{RESET}")
            sys.exit()

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
    # Large Bold Green Letter inside Red Box
    print(f"{BG_RED}{' '*50}{RESET}")
    print(f"{BG_RED}{BOLD}{GREEN}      HCO WEBSITE VULNERABILITY FINDER          {RESET}{BG_RED}  {RESET}")
    print(f"{BG_RED}{' '*50}{RESET}")
    
    print(f"\n{BLUE}[1]{RESET} Full Site Audit (Vulnerability Scan)")
    print(f"{BLUE}[2]{RESET} Check for Outdated Server Software")
    print(f"{BLUE}[3]{RESET} Scan for Hidden Directories")
    print(f"{BLUE}[4]{RESET} Exit")
    
    choice = input(f"\n{YELLOW}[?] Select an option: {RESET}")
    
    if choice == '1':
        target = input(f"{BLUE}[*] Enter Website URL (e.g., example.com): {RESET}")
        print(f"{GREEN}[*] Initializing deep scan on {target}...{RESET}")
        # Call nikto engine
        os.system(f"nikto -h {target}")
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
    # 1. Run the YouTube lock
    redirect_to_youtube()
    # 2. Fix the engine if missing
    fix_engine()
    # 3. Launch Dashboard
    main_dashboard()
