"""
문제 요약:
점 (x, y)가 어느 사분면에 있는지 출력한다.

입력:
- 첫 줄: x
- 둘째 줄: y

출력:
- 1, 2, 3, 4 중 하나

예제 입력:
12
5

예제 출력:
1
"""

x = int(input().strip())
y = int(input().strip())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)
