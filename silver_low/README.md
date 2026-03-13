# 실버 하위 추천 문제 (문법 + 기본 자료구조)

아래 문제들은 지난주 브론즈 수준에서 한 단계 올린 **실버 하위 체감** 문제들입니다.
각 문제의 풀이 코드는 같은 폴더의 `문제번호.py` 파일에 있습니다.

1. [1920 수 찾기](https://www.acmicpc.net/problem/1920)
2. [10816 숫자 카드 2](https://www.acmicpc.net/problem/10816)
3. [9012 괄호](https://www.acmicpc.net/problem/9012)
4. [10828 스택](https://www.acmicpc.net/problem/10828)
5. [2164 카드2](https://www.acmicpc.net/problem/2164)
6. [1181 단어 정렬](https://www.acmicpc.net/problem/1181)
7. [1316 그룹 단어 체커](https://www.acmicpc.net/problem/1316)
8. [4949 균형잡힌 세상](https://www.acmicpc.net/problem/4949)

---

## 문제별 문법/개념 + 풀이 힌트 (접기/펼치기)

<details>
<summary>1920 수 찾기</summary>
- 관련 문법/개념: 리스트, 집합(set), 반복문, 조건문, 출력 모으기
- 풀이 힌트: 입력된 수들을 `set`에 넣고, 질의마다 포함 여부를 `in`으로 확인한다.
</details>

<details>
<summary>10816 숫자 카드 2</summary>
- 관련 문법/개념: 딕셔너리(dict)로 카운팅, 반복문, 출력 모으기
- 풀이 힌트: 카드 숫자의 개수를 `dict`에 저장하고, 질의마다 개수를 꺼낸다.
</details>

<details>
<summary>9012 괄호</summary>
- 관련 문법/개념: 반복문, 조건문, 카운팅(스택 없이)
- 풀이 힌트: 여는 괄호면 +1, 닫는 괄호면 -1. 중간에 음수가 되면 실패.
</details>

<details>
<summary>10828 스택</summary>
- 관련 문법/개념: 리스트로 스택 구현, 조건문, 문자열 처리
- 풀이 힌트: `append`, `pop`, `len`을 이용해 명령별로 처리한다.
</details>

<details>
<summary>2164 카드2</summary>
- 관련 문법/개념: 리스트, 인덱스(포인터), 반복문
- 풀이 힌트: 리스트에서 직접 제거하지 말고, 인덱스를 앞으로 이동시키며 처리한다.
</details>

<details>
<summary>1181 단어 정렬</summary>
- 관련 문법/개념: 리스트, set 중복 제거, 정렬
- 풀이 힌트: `set`으로 중복 제거 후, 먼저 사전순 정렬하고 길이 기준으로 한 번 더 정렬한다.
</details>

<details>
<summary>1316 그룹 단어 체커</summary>
- 관련 문법/개념: 문자열, 반복문, set, 조건문
- 풀이 힌트: 이전 글자와 다를 때만 `set`에 추가하고, 이미 있으면 실패.
</details>

<details>
<summary>4949 균형잡힌 세상</summary>
- 관련 문법/개념: 리스트로 스택, 문자열 처리, 반복문
- 풀이 힌트: 괄호 종류별로 push/pop 하며, 짝이 맞지 않으면 실패.
</details>
