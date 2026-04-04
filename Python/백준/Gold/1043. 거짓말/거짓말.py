import sys

# 입력 속도 최적화
input = sys.stdin.readline

def find(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출 (경로 압축)
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    # 두 원소가 속한 집합을 합치기
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

n, m = map(int, input().split())
truth_input = list(map(int, input().split()))

# 1. 진실을 아는 사람이 아무도 없으면 모든 파티에서 거짓말 가능
if truth_input[0] == 0:
    print(m)
else:
    truth_knowers = truth_input[1:]
    parent = [i for i in range(n + 1)]

    # 2. 진실을 아는 사람들을 무조건 하나의 그룹(루트)으로 묶어버림
    for i in range(1, len(truth_knowers)):
        union(parent, truth_knowers[0], truth_knowers[i])

    parties = []
    # 3. 파티 정보를 받으면서, 같은 파티에 있는 사람들을 모두 같은 그룹으로 묶음
    for _ in range(m):
        party = list(map(int, input().split()))[1:]
        parties.append(party)
        for i in range(1, len(party)):
            union(parent, party[0], party[i])

    ans = 0
    # 4. 각 파티를 돌면서, 진실을 아는 그룹과 엮여있는지 최종 검사
    for party in parties:
        # 파티 참가자 중 한 명이라도 진실을 아는 사람과 루트가 다르면 거짓말 가능
        if find(parent, party[0]) != find(parent, truth_knowers[0]):
            ans += 1

    print(ans)