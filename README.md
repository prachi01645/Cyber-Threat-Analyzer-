# Cyber-Threat-Analyzer-
Analyzes server logs to identify abnormal access patterns and potential security threats.
# LogGuard

LogGuard is a simple cybersecurity project that analyzes server log entries to detect suspicious IP activity using basic Python logic.

## Overview
Server logs often contain early signs of malicious behavior such as brute-force attempts or abnormal access patterns.  
This project demonstrates how basic log analysis can be used to identify such suspicious activity in a clear and lightweight way.

## Features
- Counts the number of requests made by each IP address
- Flags IPs with unusually high request frequency
- Uses only core Python (no external libraries)
- Easy to understand and extend

## Dataset
The project uses sample server log entries embedded directly in the script.  
Each log entry contains:
- IP address
- Timestamp
- Request type
- Status code

## Methodology
1. Parse log entries to extract IP addresses  
2. Count the number of requests per IP  
3. Apply a simple threshold rule to identify suspicious behavior  
4. Display results in a readable format  

## Results
The script successfully identifies IP addresses that exceed a predefined request limit and flags them as potentially suspicious.

## How to Run
1. Download the repository
2. Open the project folder
3. Run the script:
   ```bash
   python log_analyzer.py
