# 🤖 AI Collaboration Log (Prompts)

## 🧩 Task 2: Log File Analyzer

### 📝 Initial Prompt
Build a **Python script** that can analyze web server log files and generate a clear summary report.

The script should:
- Read and parse log files  
- Count total and unique IP requests  
- Find the most common endpoints  
- Summarize status codes  
- Detect high error rates and suspicious IPs  
- Save the final report to a JSON file  

---

### 💬 Prompt 2 – Testing Example
Give few example log lines to test the script.  
ChatGPT provided sample log entries with different IPs, endpoints, and response codes to test the logic easily.

---

### 💬 Prompt 3 – Full Code
Write the complete Python code for the analyzer.  
ChatGPT generated a working script called **`log_analyzer.py`** that:
- Reads the log file  
- Extracts IPs, endpoints, and status codes  
- Summarizes everything in a JSON structure  
- Saves the report automatically as **`report.json`**

---

### 💬 Prompt 4 – Show Output Example
Show what the final result should look like in the console.

**Example Output:**
```json
📄 LOG FILE SUMMARY REPORT

{
    "total_requests": 2,
    "unique_ips": 2,
    "most_common_endpoints": ["/api/users", "/login"],
    "status_code_breakdown": {"200": 1, "401": 1},
    "potential_issues": {
        "high_error_rate": true,
        "error_rate_percentage": 50.0,
        "suspicious_ips": ["192.168.1.1", "10.0.0.1"]
    }
}
```
Report saved to report.json

---

💬 Prompt 5 – Add Run Instructions
Add a simple explanation on how to run the project.

⚙️ How to Run

Make sure all project files (log_analyzer.py and access.log) are in the same folder.

Open your terminal or console in that folder path.

Run the command:

```bash
python log_analyzer.py
```
The result will appear in the console and also be saved as report.json in the same folder.

