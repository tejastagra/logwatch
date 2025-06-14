from logwatch.parser import parse_log
from logwatch.detector import detect_brute_force
from logwatch.config import LOG_PATH, ATTEMPT_THRESHOLD

def main():
    print(f"🔍 Analyzing log file: {LOG_PATH}")
    ip_list = parse_log(LOG_PATH)
    flagged_ips = detect_brute_force(ip_list, ATTEMPT_THRESHOLD)

    if not flagged_ips:
        print("✅ No brute-force attempts detected.")
    else:
        print("🚨 Suspicious IPs:")
        for ip, count in flagged_ips.items():
            print(f"{ip} → {count} failed attempts")

        with open("report.csv", "w") as file:
            file.write("IP Address,Attempts\n")
            for ip, count in flagged_ips.items():
                file.write(f"{ip},{count}\n")
        print("📁 Report saved to report.csv")

if __name__ == "__main__":
    main()
