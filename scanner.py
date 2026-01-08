import sys
import socket
from datetime import datetime

# Banner for style
print("-" * 50)
print("💀 TATIYA PORT SCANNER v1.0")
print("    Scanning Target...")
print("-" * 50)

# 1. Define the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python scanner.py <ip>")
    sys.exit()

print(f"Scanning Target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    # 2. Scan ports 1 to 1024 (The most common ports)
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # Wait 1 second for response
        
        # Returns 0 if port is open
        result = s.connect_ex((target, port)) 
        if result == 0:
            print(f"[*] Port {port} is OPEN")
        s.close()

except KeyboardInterrupt:
    print("\n[!] Exiting Program.")
    sys.exit()

except socket.gaierror:
    print("\n[!] Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\n[!] Could not connect to server.")
    sys.exit()

print("-" * 50)
print("Scan completed.")

