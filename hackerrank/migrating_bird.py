import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    # counts for types 1..5 (index 0 unused)
    counts = [0] * 6
    for t in arr:
        if 1 <= t <= 5:
            counts[t] += 1

    # find the type with max count; in a tie, the smaller index is chosen automatically
    best_type = 1
    best_count = counts[1]
    for t in range(2, 6):
        if counts[t] > best_count:
            best_count = counts[t]
            best_type = t

    return best_type


# If running as a script that reads HackerRank-style input:
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        # example fallback
        n = 6
        arr = [1, 4, 4, 4, 5, 3]
    else:
        n = int(data[0])
        arr = list(map(int, data[1:1+n]))

    print(migratoryBirds(arr))
