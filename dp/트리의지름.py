import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000000)
n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])
mymax=0
fartest_node=1
def dfs(x,dis):
    global mymax , fartest_node
    if dis>mymax:
        mymax=dis
        fartest_node=x
    
    for neighbor,weight in tree[x]:
        if visited[neighbor]==0:
            visited[neighbor]=1
            dfs(neighbor,dis+weight)
        
#루트노드에서 가장 먼 노드 찾기
visited=[0]*(n+1)
visited[1]=1
dfs(1,0)

#찾은 가장 먼 노드에서 또 가장 먼 노드찾기
visited=[0]*(n+1)
visited[fartest_node]=1
dfs(fartest_node,0)

print(mymax)