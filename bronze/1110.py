"""
문제 요약:
N에서 시작해 다음 규칙을 반복한다.
- 새로운 수 = (현재 수의 일의 자리) * 10 + (각 자리수 합의 일의 자리)
처음 수로 돌아오기까지의 사이클 길이를 출력한다.

입력:
- 첫 줄: N (0~99)

출력:
- 사이클 길이

예제 입력:
26

예제 출력:
4
"""

n = int(input().strip())
start = n
count = 0

while True:
    a = n // 10
    b = n % 10
    s = a + b
    n = b * 10 + (s % 10)
    count += 1
    if n == start:
        break

print(count)
