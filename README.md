# py-vuln-scanner

A **lightweight Python-based vulnerability scanner** that identifies open ports on a target system and lays the foundation for service enumeration and vulnerability assessment workflows. Designed as a practical cyber security project to demonstrate scanning, modular Python architecture, and the initial stages of penetration testing.

---

## 🚀 Features

✅ Scans for open TCP ports on a target IP address  
✅ Uses Python’s `socket` module for raw connectivity testing  
✅ Configurable target IP, ports, and timeout  
✅ Modular structure for easy expansion (banner grabbing, threading, reporting)  
✅ Clean CLI entry point for professional project usage

---

## 🖥️ Demo

```bash
python -m scanner.main

## 🛠️ Project Structure

py-vuln-scanner/
│
├── scanner/
│ ├── main.py # Entry point
│ ├── scanner.py # Core scanning logic
│ ├── utils.py # Helper functions (planned)
│ ├── report.py # Reporting functions (planned)
│ └── config.py # Configurable constants
│
├── tests/ # Unit tests (planned)
├── requirements.txt # Dependencies
├── README.md # Project overview and instructions
└── LICENSE
