import os, subprocess, datetime, sys

def sh(cmd):
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)

# Standard-Kommitnachricht mit UTC-Zeit
msg = os.getenv("COMMIT_MSG") or f"auto: {datetime.datetime.utcnow().isoformat()}Z"

# Git Remote prüfen
remote_check = subprocess.run("git remote", shell=True, capture_output=True, text=True)
if "origin" not in remote_check.stdout:
    print("Kein Remote gefunden. Bitte zuerst 'git remote add origin ...' ausführen.")
    sys.exit(1)

print(f"[+] Committing mit Nachricht: {msg}")
sh("git add -A")
subprocess.run(f'git commit -m "{msg}"', shell=True)

print("[+] Push zu GitHub...")
sh("git push -u origin main")

print("[✓] Upload abgeschlossen — Railway wird automatisch neu deployen.")
