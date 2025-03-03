import sys
input=sys.stdin.readline

n=int(input())
g=[]
for _ in range(n):
    g.append(list(map(int,input().split())))

mymax = 0

def dfs(x):
    global mymax
    if x == n:
        now = 0
        for d in range(n):
            if g[d][0] <= 0:
                now += 1
        mymax = max(mymax, now)
        return

    if g[x][0] > 0:
        flag = False
        s, w = g[x]
        for i in range(n):
            if i != x and g[i][0] > 0:
                flag = True
                g[x][0] -= g[i][1]
                g[i][0] -= w
                dfs(x + 1)  
                g[i][0] += w
                g[x][0] += g[i][1]
        if not flag:
            dfs(x + 1)
    else:
        dfs(x + 1)

dfs(0)
print(mymax)

