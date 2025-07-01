"""
py-vuln-scanner
Main entry point for your Python-based vulnerability scanner.
"""

from scanner.scanner_core import run_scan

def main():
    print("=== py-vuln-scanner ===")
    print("Starting scan...\n")
    
    # You can expand to parse arguments later
    run_scan()

    print("\nScan completed.")

if __name__ == "__main__":
    main()