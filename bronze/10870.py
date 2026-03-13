"""
문제 요약:
N번째 피보나치 수를 출력한다.
F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)

입력:
- 첫 줄: N

출력:
- F(N)

예제 입력:
10

예제 출력:
55
"""

n = int(input().strip())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    a = 0
    b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(b)
