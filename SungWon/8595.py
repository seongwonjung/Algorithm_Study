# import sys

# input = sys.stdin.readline

# n = int(input())
# s = input().strip()
# ans = 0
# i = 0
# while i < n:
#     if s[i].isdigit():
#         j = i
#         while j < i + 6 and j < n and s[j].isdigit():
#             j += 1
#         ans += int(s[i:j])
#         i = j
#     else:
#         i += 1
# print(ans)
import sys, re

input = sys.stdin.readline
n = int(input())
s = input().strip()
# 특정 문자(0,1,2,...,9)들을 지정한 길이(1~6)로 찾기. 문자열 s에서
hidden_numbers = re.findall(r"[0-9]{1,6}", s)
ans = 0
for number in hidden_numbers:
    ans += int(number)
print(ans)
