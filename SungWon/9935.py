import sys

input = sys.stdin.readline

word = input().strip()
bomb = input().strip()
bomb_len = len(bomb)
st = list()
for c in word:
    st.append(c)
    while st and "".join(st[len(st) - bomb_len :]) == bomb:
        for _ in range(bomb_len):
            st.pop()

if len(st) == 0:
    print("FRULA")
else:
    print(*st)
