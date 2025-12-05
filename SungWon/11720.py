import sys

input = sys.stdin.readline

n = int(input())
nums = input().strip()
ans = 0
for num in nums:
    ans += int(num)
print(ans)
