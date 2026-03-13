"""
문제 요약:
1부터 N까지 카드가 있다. 맨 위 카드를 버리고, 그 다음 카드를 맨 아래로 옮기는 동작을 반복할 때
마지막으로 남는 카드를 출력한다.

입력:
- 첫 줄: N

출력:
- 마지막에 남는 카드 번호

예제 입력:
6

예제 출력:
4
"""

n = int(input().strip())
cards = list(range(1, n + 1))
head = 0

while len(cards) - head > 1:
    head += 1
    cards.append(cards[head])
    head += 1

print(cards[head])
