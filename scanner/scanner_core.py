"""
scanner/scanner.py

Core scanning logic for py-vuln-scanner.
"""

import socket
from scanner import config

def scan_port(target_ip, port, timeout=2):
    """
    Attempts to connect to the specified port on the target IP.
    Returns True if the port is open, False otherwise.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target_ip, port))
        sock.close()
        return result == 0
    except Exception as e:
        print(f"[!] Error scanning port {port} on {target_ip}: {e}")
        return False

def run_scan():
    """
    Runs a basic scan on the target IP and ports defined in config.
    """
    target_ip = config.DEFAULT_TARGET
    ports = config.DEFAULT_PORTS
    timeout = config.TIMEOUT

    print(f"Scanning {target_ip} on ports: {ports}\n")

    for port in ports:
        is_open = scan_port(target_ip, port, timeout)
        if is_open:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")

