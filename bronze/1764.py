"""
문제 요약:
듣도 못한 사람과 보도 못한 사람의 교집합을 구해 사전순으로 출력한다.

입력:
- 첫 줄: N M
- 다음 N줄: 듣도 못한 사람 이름
- 다음 M줄: 보도 못한 사람 이름

출력:
- 첫 줄: 듣보잡 수
- 다음 줄: 이름을 사전순으로 출력

예제 입력:
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

예제 출력:
2
baesangwook
ohhenrie
"""

n, m = map(int, input().split())

not_heard = set()
for _ in range(n):
    not_heard.add(input().strip())

both = []
for _ in range(m):
    name = input().strip()
    if name in not_heard:
        both.append(name)

both.sort()

print(len(both))
for name in both:
    print(name)
