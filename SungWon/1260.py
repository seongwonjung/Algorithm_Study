import sys, collections

input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
vst = [False] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()


def dfs(u):
    vst[u] = True
    print(u, end=" ")
    for v in graph[u]:
        if not vst[v]:
            dfs(v)


def bfs(u):
    q = collections.deque()
    q.append(u)
    vst[u] = True
    while q:
        tmp = q.popleft()
        print(tmp, end=" ")
        for v in graph[tmp]:
            if not vst[v]:
                q.append(v)
                vst[v] = True


dfs(start)
print()
vst = [False] * (n + 1)
bfs(start)
