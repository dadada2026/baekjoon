# 11724 연결 요소의 개수
# 그래프에서 연결된 덩어리의 개수를 세는 문제

n, m = map(int, input().split())

adj = []
for _ in range(n + 1):
    adj.append([])

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n + 1)
count = 0

for start in range(1, n + 1):
    if visited[start]:
        continue
    count += 1
    stack = [start]
    visited[start] = True
    while stack:
        v = stack.pop()
        for nv in adj[v]:
            if not visited[nv]:
                visited[nv] = True
                stack.append(nv)

print(count)
