"""
문제 요약:
다이얼에서 알파벳을 누르는 데 걸리는 시간을 계산한다.

입력:
- 한 줄: 대문자 단어

출력:
- 걸리는 시간

예제 입력:
UNUCIC

예제 출력:
36
"""

s = input().strip()

time = 0
for ch in s:
    if ch in 'ABC':
        time += 3
    elif ch in 'DEF':
        time += 4
    elif ch in 'GHI':
        time += 5
    elif ch in 'JKL':
        time += 6
    elif ch in 'MNO':
        time += 7
    elif ch in 'PQRS':
        time += 8
    elif ch in 'TUV':
        time += 9
    else:
        time += 10

print(time)
