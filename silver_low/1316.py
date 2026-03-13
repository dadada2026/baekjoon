"""
문제 요약:
단어가 같은 알파벳이 연속해서만 나타나면 그룹 단어이다.
N개의 단어 중 그룹 단어의 개수를 센다.

입력:
- 첫 줄: N
- 다음 N줄: 단어

출력:
- 그룹 단어의 개수

예제 입력:
3
happy
new
year

예제 출력:
3
"""

n = int(input().strip())
words = []
for _ in range(n):
    words.append(input().strip())

count = 0
for w in words:
    seen = set()
    prev = ''
    ok = True
    for ch in w:
        if ch != prev:
            if ch in seen:
                ok = False
                break
            seen.add(ch)
            prev = ch
    if ok:
        count += 1

print(count)
