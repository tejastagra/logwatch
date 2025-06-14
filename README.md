# LogWatch

> A lightweight Python tool to detect brute-force attacks by analyzing authentication logs.

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)

LogWatch is a simple yet powerful Python script that scans system authentication logs for repeated failed login attempts. It flags IP addresses that exceed a defined threshold and generates a CSV report for further investigation or banning.

---

## Features

* Log Parsing – Scans system auth logs (e.g. `/var/log/system.log` on macOS)
* Attack Detection – Detects IPs with excessive failed login attempts
* CSV Reports – Outputs suspicious IPs and attempt counts to `report.csv`
* Configurable – Easy to change thresholds and log file path
* Testable – Comes with a sample log file for demo/testing

---

## Sample Output

```bash
Analyzing log file: sample_logs/sample_auth.log

Suspicious IPs:
192.168.1.100 → 5 failed attempts

Report saved to report.csv
```

---

## Project Structure

```
logwatch/
├── logwatch/
│   ├── __init__.py
│   ├── parser.py
│   ├── detector.py
│   └── config.py
├── sample_logs/
│   └── sample_auth.log
├── report.csv         # Generated after running the script
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/logwatch.git
cd logwatch
```

### 2. Set Up Environment *(Optional but Recommended)*

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Run the Analyzer

```bash
python3 main.py
```

> If using a real system log (like `/var/log/system.log`), run with `sudo`:

```bash
sudo python3 main.py
```

---

## Testing with Sample Logs

To test without accessing real system logs, the project includes a sample log:

```python
# logwatch/config.py
LOG_PATH = "sample_logs/sample_auth.log"
```

Edit this file to point to `sample_logs/sample_auth.log` to simulate detection.

---

## Configuration

Adjust the detection sensitivity in `logwatch/config.py`:

```python
LOG_PATH = "/var/log/system.log"  # or your custom test file
ATTEMPT_THRESHOLD = 5            # Number of failures before flagging an IP
```

---

## Requirements

Python 3.6 or above. No external libraries required.

Install dependencies (if you add optional ones like `matplotlib` or `ipinfo`):

```bash
pip3 install -r requirements.txt
```

---

## Example Report (`report.csv`)

```
IP Address,Attempts
192.168.1.100,5
203.0.113.5,8
```

---

## Contributing

Pull requests are welcome. Feel free to submit improvements, bug fixes, or feature suggestions. For major changes, please open an issue first.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**Tejas Tagra** – [hello@tejastagra.com](mailto:hello@tejastagra.com)
Built as a side project to explore security monitoring and log analysis using Python.
