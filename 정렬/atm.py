n=int(input())
l=list(map(int,input().split()))

l.sort()

for i in range(1,n):
    l[i]=l[i-1]+l[i]

print(sum(l))