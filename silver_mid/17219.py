# 17219 비밀번호 찾기
# 사이트 -> 비밀번호 딕셔너리

n, m = map(int, input().split())

pw = {}
for _ in range(n):
    site, password = input().split()
    pw[site] = password

out = []
for _ in range(m):
    site = input().strip()
    out.append(pw[site])

print('\n'.join(out))
