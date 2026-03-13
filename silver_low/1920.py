"""
문제 요약:
N개의 정수 목록이 주어진다. 이어서 M개의 수가 주어질 때,
각 수가 목록에 존재하면 1, 없으면 0을 출력한다.

입력:
- 첫 줄: N
- 둘째 줄: N개의 정수
- 셋째 줄: M
- 넷째 줄: M개의 정수

출력:
- 각 수마다 존재 여부를 한 줄에 1 또는 0으로 출력

예제 입력:
5
4 1 5 2 3
5
1 3 7 9 5

예제 출력:
1
1
0
0
1
"""

n = int(input().strip())
nums = set(map(int, input().split()))
m = int(input().strip())
queries = list(map(int, input().split()))

out = []
for x in queries:
    out.append('1' if x in nums else '0')

print('\n'.join(out))
