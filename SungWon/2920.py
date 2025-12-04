import sys

input = sys.stdin.readline

# ascending, descending, mixed
scale = list(map(int, input().split()))
ascending = [1, 2, 3, 4, 5, 6, 7, 8]
desending = [8, 7, 6, 5, 4, 3, 2, 1]
if scale == ascending:
    print("ascending")
elif scale == desending:
    print("descending")
else:
    print("mixed")
