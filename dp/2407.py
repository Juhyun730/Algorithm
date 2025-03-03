n,m=map(int,input().split())
a=1
b=1
for i in range(m):
    a=a*(n-i)
for i in range(m):
    b=b*(m-i)
print(int(a//b))