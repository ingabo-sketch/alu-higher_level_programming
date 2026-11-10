#!/usr/bin/python3
"""Script that reads stdin and prints accumulated request metrics."""
import sys

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
total_size = 0
line_count = 0


def print_stats():
    """Print the total file size and the count of each seen status code."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        try:
            total_size += int(parts[-1])
            code = parts[-2]
            if code in status_codes:
                status_codes[code] += 1
        except (IndexError, ValueError):
            pass
        if line_count % 10 == 0:
            print_stats()
    if line_count % 10:
        print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
