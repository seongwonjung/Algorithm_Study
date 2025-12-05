import sys

input = sys.stdin.readline

x = input().strip()
if x[0] + x[1] == "0x":
    print(int(x, 16))
elif x[0] == "0":
    print(int(x, 8))
else:
    print(x)
