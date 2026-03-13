# 18870 좌표 압축
# 정렬된 고유값에 순서를 매겨 출력

n = int(input().strip())
nums = list(map(int, input().split()))

uniq = list(set(nums))
uniq.sort()

rank = {}
idx = 0
for v in uniq:
    rank[v] = idx
    idx += 1

out = []
for v in nums:
    out.append(str(rank[v]))

print(' '.join(out))
