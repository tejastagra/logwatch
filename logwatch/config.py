# logwatch/config.py

# Path to the system log file (change this to "sample_logs/sample_auth.log" for testing)
LOG_PATH = "/var/log/system.log"

# Number of failed attempts before flagging an IP as suspicious
ATTEMPT_THRESHOLD = 5