# logwatch/detector.py

from collections import Counter

def detect_brute_force(ip_list, threshold):
    """
    Detects IP addresses that have failed login attempts greater than or equal to the threshold.

    Args:
        ip_list (list): A list of IP addresses from failed login attempts.
        threshold (int): Number of failures before flagging an IP.

    Returns:
        dict: A dictionary of suspicious IPs and their corresponding failure counts.
    """
    counts = Counter(ip_list)
    return {ip: c for ip, c in counts.items() if c >= threshold}