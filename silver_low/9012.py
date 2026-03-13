"""
문제 요약:
여러 개의 괄호 문자열이 주어질 때, 각 문자열이 올바른 괄호 문자열(VPS)인지 판단한다.

입력:
- 첫 줄: T
- 다음 T줄: 괄호 문자열

출력:
- 각 줄마다 YES 또는 NO

예제 입력:
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

예제 출력:
NO
NO
YES
NO
YES
NO
"""

t = int(input().strip())

out = []
for _ in range(t):
    s = input().strip()
    bal = 0
    ok = True
    for ch in s:
        if ch == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            ok = False
            break
    if bal != 0:
        ok = False
    out.append('YES' if ok else 'NO')

print('\n'.join(out))
