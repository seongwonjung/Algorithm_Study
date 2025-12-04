import sys
from sys import stdin

input = sys.stdin.readline

a, b, c = [int(input()) for _ in range(3)]
total = a * b * c
counts = [0] * 10
while total > 0:
    counts[total % 10] += 1
    total //= 10

for i in counts:
    print(i)
