"""
문제 요약:
각 줄의 괄호 '()'와 '[]'가 올바르게 짝을 이루는지 판별한다.
입력은 한 줄에 하나의 문자열이며, 줄이 "." 하나면 종료한다.

입력:
- 여러 줄의 문자열
- 마지막 줄은 단 하나의 점 "."

출력:
- 각 줄마다 yes 또는 no

예제 입력:
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.

예제 출력:
yes
yes
no
no
no
yes
yes
"""


def is_ok(s):
    st = []
    for ch in s:
        if ch == '(' or ch == '[':
            st.append(ch)
        elif ch == ')':
            if not st or st[-1] != '(':
                return False
            st.pop()
        elif ch == ']':
            if not st or st[-1] != '[':
                return False
            st.pop()
    return not st

out = []
while True:
    try:
        line = input()
    except EOFError:
        break
    if line == '.':
        break
    out.append('yes' if is_ok(line) else 'no')

print('\n'.join(out))
