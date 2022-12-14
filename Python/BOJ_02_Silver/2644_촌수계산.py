from collections import deque

def bfs(node):
    Q = deque()
    Q.append(node)
    while Q:
        node = Q.popleft()
        for n in graph[node]:
            if visited[n] == 0:
                visited[n] = visited[node] + 1
                Q.append(n)

n = int(input())
graph = [[] for _ in range(n + 1)]
s, e = map(int, input().split())
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (n + 1)
bfs(s)
print(visited[e] if visited[e] > 0 else -1)