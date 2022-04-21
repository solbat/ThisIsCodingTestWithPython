# 9-3.py 플로이드 워셜 알고리즘 소스코드

INF = int(1e9)

n = 5

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph1 = [[INF] * (n+1) for _ in range(n+1)]
graph2 = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph1[a][b] = 0

print(graph1)

for i in range(1, n+1):
    graph2[i][i] = 0

print(graph2)

if graph1 == graph2:
    print("YES!!!!!!!!!!")
