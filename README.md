# URL-IP-Cleaner

A **Flask-based web application** that helps extract, clean, and format **Indicators of Compromise (IOCs)** such as URLs, IP addresses, and domains.  
Built to streamline threat intelligence workflows by converting obfuscated indicators into a readable and actionable format.

🔗 **Live Demo:** [url-ip-cleaner.vercel.app](https://url-ip-cleaner.vercel.app/)

## ✨ Features

- **Extracts IOCs**: Parses URLs, IPs, and domains from text and files.
- **Cleans & Normalizes Data**: Converts non-standard formats (e.g., `hxxp[:]` → `http:`, `[.]` → `.`).
- **Removes Ports**: Strips unnecessary ports from IPs and domains.
- **Parses HTML Tables**: Extracts structured data from uploaded files.
- **Clipboard Copy**: One-click copying for quick use.

## 🚀 Technologies

- **Backend:** Flask (Python)
- **Frontend:** HTML, JavaScript, CSS
- **Deployment:** Vercel

## 📌 Use Case

Designed for **cybersecurity workflows**, particularly for handling **IOC lists** from threat reports, intelligence feeds, or raw text dumps.  
Helps analysts quickly sanitize and extract indicators without manual effort.
