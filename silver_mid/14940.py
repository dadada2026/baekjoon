# 14940 쉬운 최단거리
# BFS로 거리 계산

n, m = map(int, input().split())

grid = []
start_x = 0
start_y = 0

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(m):
        if row[j] == 2:
            start_x = i
            start_y = j

# 거리 배열
# -1로 초기화, 0인 칸은 그대로 0 출력

dist = []
for _ in range(n):
    dist.append([-1] * m)

queue = [(start_x, start_y)]
head = 0

# 시작점은 0

dist[start_x][start_y] = 0

# 이동 방향

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while head < len(queue):
    x, y = queue[head]
    head += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if grid[nx][ny] == 0:
            continue
        if dist[nx][ny] != -1:
            continue
        dist[nx][ny] = dist[x][y] + 1
        queue.append((nx, ny))

# 출력

for i in range(n):
    out = []
    for j in range(m):
        if grid[i][j] == 0:
            out.append('0')
        else:
            out.append(str(dist[i][j]))
    print(' '.join(out))
