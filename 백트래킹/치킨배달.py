import sys
input = sys.stdin.readline

n, m = map(int, input().split())

chicken = []
house = []

# 입력을 받으면서 집과 치킨집을 분리
for x in range(n):
    l = list(map(int, input().split()))
    for y in range(n):
        if l[y] == 1:
            house.append((x, y))
        elif l[y] == 2:
            chicken.append((x, y))

min_distance = float('inf')

# 주어진 치킨집 조합에서 각 집에 대한 최소 거리를 계산
def calculate_distance(selected_chickens):
    total_distance = 0
    for hx, hy in house:
        min_distance = float('inf')
        for cx, cy in selected_chickens:
            min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
        total_distance += min_distance
    return total_distance

def backtrack(index, selected_chickens):
    global min_distance
    
    # M개의 치킨집을 선택하면 거리 계산
    if len(selected_chickens) == m:
        min_distance = min(min_distance, calculate_distance(selected_chickens))
        return

    # 백트래킹: 남은 치킨집을 선택
    for i in range(index, len(chicken)):
        selected_chickens.append(chicken[i])
        backtrack(i + 1, selected_chickens)
        selected_chickens.pop()

# 백트래킹 시작
backtrack(0, [])
print(min_distance)