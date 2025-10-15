# 🧩 Task 2: Log File Analyzer

## 📋 Description
This Python script analyzes web server access logs (in common Apache/Nginx format) and generates a summary report.  
It helps DevOps teams quickly understand web traffic patterns and detect potential issues.

---

## ⚙️ Features
- **Parses** log files using a robust regular expression  
- **Generates** key statistics:
  - Total number of requests  
  - Number of unique IP addresses  
  - Most frequently accessed endpoints  
  - Status code breakdown  
- **Detects potential issues:**
  - High error rate (>10%)  
  - Suspicious IPs sending more than 5% of total requests  

---

## 🧮 Output
- A summary report printed in the console (formatted as JSON)  
- A `report.json` file saved locally with the same data  

---

## 🪄 How to Run

1. **Make sure all files are in the same folder**  
   Keep these files together in one directory, for example:
```bash
log_analyzer.py
access.log
```
markdown
Copy code

2. **Open the console in the same path**  
- On **Windows**: open the folder, then **Shift + Right Click** → select **“Open PowerShell window here”**  
- On **Linux/Mac**: open the terminal and navigate to the folder path, for example:
  ```bash
  cd /path/to/your/project
  ```

3. **Run the script**
```bash
python log_analyzer.py
```
(or use python3 log_analyzer.py depending on your system)

View the results

The summary will be printed in the console

A file named report.json will be created automatically in the same folder containing the same results

🖥️ See the Results
When you run the script, you’ll see a console output similar to this:

```json


{
    "total_requests": 2,
    "unique_ips": 2,
    "most_common_endpoints": [
        "/api/users",
        "/login"
    ],
    "status_code_breakdown": {
        "200": 1,
        "401": 1
    },
    "potential_issues": {
        "high_error_rate": true,
        "error_rate_percentage": 50.0,
        "suspicious_ips": [
            "192.168.1.1",
            "10.0.0.1"
        ]
    }
}
```
Report saved to 'report.json'
✅ This means the analysis is complete, and a file named report.json has been created automatically in the same folder.
You can open it with any text editor or JSON viewer to check the results again later.

📝 Notes
The script uses only built-in Python modules (re, json, collections).

Make sure your log file matches the Apache/Nginx access log format.


