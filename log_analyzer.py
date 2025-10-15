
import re
import json
from collections import Counter, defaultdict

# Regex
log_pattern = re.compile(
    r'(?P<ip>\S+) - - \[(?P<date>.*?)\] "(?P<method>\S+) (?P<endpoint>\S+) \S+" (?P<status>\d+) (?P<size>\d+)'
)


with open("access.log", "r") as f:
    logs = f.readlines()

# Data aggregation
ips = []
endpoints = []
statuses = []
ip_requests = defaultdict(int)

for line in logs:
    match = log_pattern.match(line)
    if match:
        data = match.groupdict()
        ips.append(data["ip"])
        endpoints.append(data["endpoint"])
        statuses.append(data["status"])
        ip_requests[data["ip"]] += 1

# General statistics
total_requests = len(logs)
unique_ips = len(set(ips))
status_counts = Counter(statuses)
most_common_endpoints = [ep for ep, _ in Counter(endpoints).most_common(5)]

# Error analysis
error_codes = [code for code in statuses if code.startswith(("4", "5"))]
error_rate = len(error_codes) / total_requests if total_requests else 0
high_error_rate = error_rate > 0.1

# Suspicious IPs (more than 5% of total requests)
suspicious_ips = [ip for ip, count in ip_requests.items() if count > (total_requests * 0.05)]

# Final report
report = {
    "total_requests": total_requests,
    "unique_ips": unique_ips,
    "most_common_endpoints": most_common_endpoints,
    "status_code_breakdown": dict(status_counts),
    "potential_issues": {
        "high_error_rate": high_error_rate,
        "error_rate_percentage": round(error_rate * 100, 2),
        "suspicious_ips": suspicious_ips
    }
}

# Print report
print("\nLOG FILE SUMMARY REPORT\n")
print(json.dumps(report, indent=4))

# Save report to JSON file
with open("report.json", "w") as f:
    json.dump(report, f, indent=4)

print("\nReport saved to 'report.json'")
