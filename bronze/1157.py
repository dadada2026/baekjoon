"""
문제 요약:
단어에서 가장 많이 사용된 알파벳을 출력한다.
여러 개이면 ? 를 출력한다.

입력:
- 한 줄: 단어 (대소문자)

출력:
- 가장 많이 사용된 알파벳(대문자) 또는 ?

예제 입력:
Mississipi

예제 출력:
?
"""

s = input().strip().upper()

cnt = {}
for ch in s:
    cnt[ch] = cnt.get(ch, 0) + 1

max_count = 0
max_char = ''
multiple = False

for ch in cnt:
    if cnt[ch] > max_count:
        max_count = cnt[ch]
        max_char = ch
        multiple = False
    elif cnt[ch] == max_count:
        multiple = True

if multiple:
    print('?')
else:
    print(max_char)
