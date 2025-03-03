import sys

input=sys.stdin.readline

n=int(input())
l=list(map(int,input().split()))
l.sort()

x=int(input())
count=0
mysum=0
end=0

for start in range(n):
    mysum=0
    end=start+1
    while end<n:
        mysum=l[start]+l[end]
        if mysum==x:
            count+=1
            break
        elif mysum>x:
            break
        elif mysum <x:
            end+=1

print(count)