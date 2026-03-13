# 실버 중급 추천 문제

아래 문제들은 실버 중급(보통 Silver III~II 체감) 수준의 연습 문제들입니다.
각 문제의 풀이 코드는 같은 폴더의 `문제번호.py` 파일에 있습니다.

1. [11724 연결 요소의 개수](https://www.acmicpc.net/problem/11724)
2. [11727 2×n 타일링 2](https://www.acmicpc.net/problem/11727)
3. [16928 뱀과 사다리 게임](https://www.acmicpc.net/problem/16928)
4. [17219 비밀번호 찾기](https://www.acmicpc.net/problem/17219)
5. [17626 Four Squares](https://www.acmicpc.net/problem/17626)
6. [18870 좌표 압축](https://www.acmicpc.net/problem/18870)
7. [14940 쉬운 최단거리](https://www.acmicpc.net/problem/14940)
8. [21736 헌내기는 친구가 필요해](https://www.acmicpc.net/problem/21736)

---

## 문제별 문법/개념 + 풀이 힌트 (접기/펼치기)

<details>
<summary>11724 연결 요소의 개수</summary>
- 관련 문법/개념: 그래프(인접 리스트), 방문 배열, 스택/큐
- 풀이 힌트: 아직 방문하지 않은 정점에서 DFS/BFS를 돌리며 개수를 센다.
</details>

<details>
<summary>11727 2×n 타일링 2</summary>
- 관련 문법/개념: DP, 점화식, 나머지 연산
- 풀이 힌트: dp[n] = dp[n-1] + 2*dp[n-2] (mod 10007)
</details>

<details>
<summary>16928 뱀과 사다리 게임</summary>
- 관련 문법/개념: BFS, 최단거리, 배열
- 풀이 힌트: 1부터 시작해 주사위 1~6 이동을 BFS로 탐색하고, 뱀/사다리는 즉시 이동 처리한다.
</details>

<details>
<summary>17219 비밀번호 찾기</summary>
- 관련 문법/개념: 딕셔너리, 입력 처리
- 풀이 힌트: 사이트-비밀번호를 dict에 저장하고, 질의마다 바로 출력한다.
</details>

<details>
<summary>17626 Four Squares</summary>
- 관련 문법/개념: DP, 제곱수 반복
- 풀이 힌트: dp[i] = min(dp[i - j*j] + 1)로 채운다.
</details>

<details>
<summary>18870 좌표 압축</summary>
- 관련 문법/개념: 정렬, 중복 제거, 딕셔너리
- 풀이 힌트: 정렬된 고유값에 인덱스를 매겨 원래 값에 대응시킨다.
</details>

<details>
<summary>14940 쉬운 최단거리</summary>
- 관련 문법/개념: BFS, 격자 탐색, 거리 배열
- 풀이 힌트: 시작점(2)에서 BFS로 거리 채우고, 원래 0인 칸은 0, 도달 못한 1은 -1.
</details>

<details>
<summary>21736 헌내기는 친구가 필요해</summary>
- 관련 문법/개념: BFS/DFS, 격자 탐색
- 풀이 힌트: 시작점에서 갈 수 있는 칸만 탐색하며 P를 센다. 0이면 "TT".
</details>
