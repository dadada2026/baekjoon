# 16928 뱀과 사다리 게임
# BFS로 최소 이동 횟수 계산

n, m = map(int, input().split())

jump = [0] * 101
for _ in range(n + m):
    a, b = map(int, input().split())
    jump[a] = b

visited = [False] * 101
dist = [-1] * 101

queue = [1]
head = 0
visited[1] = True
dist[1] = 0

while head < len(queue):
    cur = queue[head]
    head += 1
    if cur == 100:
        break
    for d in range(1, 7):
        nxt = cur + d
        if nxt > 100:
            continue
        if jump[nxt] != 0:
            nxt = jump[nxt]
        if not visited[nxt]:
            visited[nxt] = True
            dist[nxt] = dist[cur] + 1
            queue.append(nxt)

print(dist[100])
