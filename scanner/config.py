"""
scanner/config.py

Configuration constants for py-vuln-scanner.
"""

DEFAULT_TARGET = "127.0.0.1"

# Common ports: SSH, HTTP, HTTPS, RDP
DEFAULT_PORTS = [22, 80, 443, 3389]

TIMEOUT = 2  # seconds