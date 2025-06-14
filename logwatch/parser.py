import re

PATTERN = re.compile(r"Failed.*from (\\d+\\.\\d+\\.\\d+\\.\\d+)")

def parse_log(path):
    entries = []
    with open(path, "r") as file:
        for line in file:
            match = PATTERN.search(line)
            if match:
                entries.append(match.group(1))
    return entries