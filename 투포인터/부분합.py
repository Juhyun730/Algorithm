import sys

input=sys.stdin.readline
n,s=map(int,input().split())
l=list(map(int,input().split()))

#l.sort()

end=0
start=0
minlen=999999999
csum=0
while 1:
    if csum>=s:
        minlen=min(minlen,end-start)
        csum-=l[start]
        start+=1

    elif end==n:
        break
    else:
        csum+=l[end]
        end+=1

if minlen==999999999:
    print(0)
else:
    print(minlen)