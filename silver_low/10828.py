"""
문제 요약:
정수 스택을 구현하고, 주어진 명령을 처리한다.
명령: push X, pop, size, empty, top

입력:
- 첫 줄: N
- 다음 N줄: 명령

출력:
- 출력이 필요한 명령의 결과를 한 줄씩 출력

예제 입력:
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top

예제 출력:
2
2
0
2
1
-1
0
1
-1
0
3
"""

n = int(input().strip())
stack = []
out = []

for _ in range(n):
    line = input().split()
    cmd = line[0]
    if cmd == 'push':
        stack.append(int(line[1]))
    elif cmd == 'pop':
        out.append(str(stack.pop() if stack else -1))
    elif cmd == 'size':
        out.append(str(len(stack)))
    elif cmd == 'empty':
        out.append('0' if stack else '1')
    elif cmd == 'top':
        out.append(str(stack[-1] if stack else -1))

print('\n'.join(out))
