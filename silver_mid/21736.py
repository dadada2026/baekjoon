# 21736 헌내기는 친구가 필요해
# BFS로 도달 가능한 P 개수 세기

n, m = map(int, input().split())

campus = []
start_x = 0
start_y = 0

for i in range(n):
    line = input().strip()
    campus.append(line)
    for j in range(m):
        if line[j] == 'I':
            start_x = i
            start_y = j

visited = []
for _ in range(n):
    visited.append([False] * m)

queue = [(start_x, start_y)]
head = 0
visited[start_x][start_y] = True

count = 0

# 이동 방향

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while head < len(queue):
    x, y = queue[head]
    head += 1
    if campus[x][y] == 'P':
        count += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visited[nx][ny]:
            continue
        if campus[nx][ny] == 'X':
            continue
        visited[nx][ny] = True
        queue.append((nx, ny))

if count == 0:
    print('TT')
else:
    print(count)
