import sys

input=sys.stdin.readline

n=int(input())


g=[]
for i in range(n):
    g.append(int(input()))

end=0
start=0
# a-b 100000
# b-c 2
# e-a 5
maxlen=0
allsum=sum(g)

din=g[start]
dout=allsum-din

while end<n:
    nowd=min(din,dout)
    if maxlen<nowd:
        maxlen=nowd
    if 2*din>allsum: # 전체 거리의 반지름보다 크면 : 
        start+=1
        din=din-g[start-1]
    else:
        end+=1
        if end==n:
            break
        din=din+g[end]
    dout=allsum-din

print(maxlen)
        

#우수코드
'''import sys
n=int(sys.stdin.readline().rstrip())
dist = []
for i in range(n):
    dist.append(int(sys.stdin.readline().rstrip()))
dist.append(0)
tot=sum(dist)

result=float('-inf')

start = 0
end = 0

prefix=dist[0]

while start <= end and end<n:
    tmp = min(prefix, tot-prefix)
    result = max(result, tmp)
    
    if tmp == prefix:
        end+=1
        prefix+=dist[end]
    else:
        prefix-=dist[start]
        start+=1
        
    
print(result)'''
        
        