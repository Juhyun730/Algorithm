from collections import deque
visited=set()
def a(x,y):
    flag=0
    print(x,y)
    for i in range(len(x)):
        if x[i]==y[i]:
            continue
        elif x[i]!=y[i]:
            flag+=1
    return flag

def solution(begin, target, words):
    answer = 999999
    q=deque()
    q.append((begin,0))
    while q:
        now,level=q.popleft()
        for s in words:
            if s not in visited:
                flag=a(now,s)
                if flag==1: #하나만 다를 때
                    if target==s: #target에 도달했을 때
                        answer=min(answer,level+1)
                        continue
                    else:
                        q.append((s,level+1))
                        visited.add(s)
    return answer

x,y=map(str,input().split())
z=list(map(str,input().split()))

ans=solution(x,y,z)
if ans==999999:
    ans=0
print(ans)