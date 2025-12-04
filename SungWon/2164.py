import sys, collections

input = sys.stdin.readline

n = int(input())

cards = collections.deque([i for i in range(1, n + 1)])

while len(cards) > 1:
    # 맨 앞 카드 버리기
    cards.popleft()
    # 그 후 맨 앞 카드를 맨 뒤로 보내기
    cards.append(cards.popleft())

print(cards[0])
