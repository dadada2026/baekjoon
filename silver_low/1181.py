"""
문제 요약:
N개의 단어를 길이 오름차순으로 정렬하고, 길이가 같으면 사전순으로 정렬한다.
같은 단어는 한 번만 출력한다.

입력:
- 첫 줄: N
- 다음 N줄: 단어

출력:
- 조건에 맞게 정렬된 단어를 한 줄씩 출력

예제 입력:
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

예제 출력:
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
"""

n = int(input().strip())
words = []
for _ in range(n):
    words.append(input().strip())

unique = list(set(words))
unique.sort()
unique.sort(key=len)

print('\n'.join(unique))
