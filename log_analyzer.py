# LogGuard - Simple Cyber Attack Log Analyzer

logs = [
    "192.168.1.10 - - [12/Jan/2024:10:15:32] GET /login 200",
    "192.168.1.10 - - [12/Jan/2024:10:15:35] GET /login 200",
    "192.168.1.10 - - [12/Jan/2024:10:15:37] GET /login 200",
    "192.168.1.25 - - [12/Jan/2024:03:45:10] POST /admin 403",
    "192.168.1.10 - - [12/Jan/2024:10:15:40] GET /login 200"
]

ip_count = {}

for log in logs:
    ip = log.split()[0]
    ip_count[ip] = ip_count.get(ip, 0) + 1

print("Request count per IP:")
for ip, count in ip_count.items():
    print(ip, "->", count)

print("\nSuspicious IPs:")
for ip, count in ip_count.items():
    if count > 3:
        print(ip, "(Possible attack)")
