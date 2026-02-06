### 🛡️ HCO-Web-Sentry

![License](https://img.shields.io/badge/License-GPLv2-red.svg)
![Platform](https://img.shields.io/badge/Platform-Termux-green.svg)
![Language](https://img.shields.io/badge/Language-Python-blue.svg)

**HCO-Web-Sentry** is an advanced web vulnerability scanner and reconnaissance tool built for ethical hackers and cybersecurity researchers. This tool automates the process of finding "loop holes" in web applications, identifying outdated server software, and brute-forcing hidden directories to help developers secure their websites.



---

## 🚀 Features

* **Full Site Audit:** Scans for 6,700+ potentially dangerous files and misconfigurations.
* **Software Identification:** Fingerprints server versions to find unpatched software (CVE-based analysis).
* **Directory Brute-Forcer:** Uses mutation techniques to find hidden admin panels and backups.
* **Automated Reporting:** All findings are saved automatically into the `HCO_Reports` folder for later analysis.
* **Subscriber-Only Access:** Integrated lock system to grow your community.

---

## ⚠️ Disclaimer

> **IMPORTANT:** This tool is for **Educational Purposes Only**. Unauthorized scanning of websites you do not own or have explicit permission to test is illegal. The developer (Azhar) is not responsible for any misuse of this tool. Use it to learn and secure the web, not to destroy it.

---

## 📲 Installation in Termux

Copy and paste the following commands into your Termux terminal to get started:

```bash
# Update system and install dependencies
pkg update && pkg upgrade -y
pkg install python git termux-api -y

# Clone the repository
git clone [https://github.com/YOUR_USERNAME/HCO-Web-Sentry](https://github.com/YOUR_USERNAME/HCO-Web-Sentry)

# Enter the directory
cd HCO-Web-Sentry

# Run the tool
python HCO-Web-Sentry.py

```
Note: Make sure you have the Termux:API app installed from F-Droid to allow the YouTube redirection to work.
🛠️ How it Works
The tool uses a modular Python wrapper to interface with the Nikto Vulnerability Engine. By leveraging specific tuning flags, it can isolate different types of vulnerabilities:
-Tuning b: Focuses on server banner grabbing and software versions.
-mutate 1: Attempts to guess hidden file names based on common patterns.
-Cgidirs all: Scans all possible CGI directories for execution vulnerabilities.

### 👨‍💻 Developed By Azhar
YouTube: https://youtube.com/@hackers_colony_tech?si=eDMKGduIEq1MUVWg
Goal: Making Cybersecurity accessible for everyone.
"A hacker is someone who is not satisfied with the way things are, but has the curiosity and the passion to see how they could be."
— Code by Azhar
