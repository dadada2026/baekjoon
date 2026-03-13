"""
문제 요약:
숫자 카드 N장이 주어질 때, M개의 수에 대해 각각 몇 장 있는지 센다.

입력:
- 첫 줄: N
- 둘째 줄: N개의 정수
- 셋째 줄: M
- 넷째 줄: M개의 정수

출력:
- M개의 수에 대한 개수를 한 줄에 공백으로 출력

예제 입력:
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

예제 출력:
3 0 0 1 2 0 0 2
"""

n = int(input().strip())
nums = list(map(int, input().split()))
m = int(input().strip())
queries = list(map(int, input().split()))

cnt = {}
for x in nums:
    cnt[x] = cnt.get(x, 0) + 1

out = []
for x in queries:
    out.append(str(cnt.get(x, 0)))

print(' '.join(out))
