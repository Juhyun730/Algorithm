import sys

input=sys.stdin.readline

n,m=map(int,input().split())

l=[]
def dfs():
    if len(l)==m:
        print(' '.join(map(str,l)))
        return
    for i in range(1,n+1):
        if i not in l:
            l.append(i)
            dfs()
            l.remove(i)
dfs()

# def dfs():
#     global cnt
    
#     for i in range(1,n+1):
        
#         if visited[i]==0 and sum(visited)!=m :

#             cnt.append(i)
#             visited[i]=1
#             dfs()
#             visited[i]=0
#             cnt.remove(i)
#         elif sum(visited)==m :
#             for t in cnt:
#                 print(t, end=' ')
#             return


# for a in range(1,2):

#     visited=[0]*(n+1)
#     visited[a]=1
#     cnt=[a]
#     dfs()