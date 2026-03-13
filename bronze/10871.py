"""
문제 요약:
N개의 정수 중 X보다 작은 수만 출력한다.

입력:
- 첫 줄: N, X
- 둘째 줄: N개의 정수

출력:
- X보다 작은 수를 순서대로 출력

예제 입력:
10 5
1 10 4 9 2 3 8 5 7 6

예제 출력:
1 4 2 3
"""

n, x = map(int, input().split())
nums = list(map(int, input().split()))

out = []
for v in nums:
    if v < x:
        out.append(str(v))

print(' '.join(out))
