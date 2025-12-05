import sys

input = sys.stdin.readline

n = int(input())
# 72 -> 2*36 -> 2*2*18 -> 2*2*2*9 -> 2*2*2*3*3
while n > 1:
    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
            n = n // i
            break
