from collections import Counter

def detect_brute_force(ip_list, threshold):
    counts = Counter(ip_list)
    return {ip: c for ip, c in counts.items() if c >= threshold}
