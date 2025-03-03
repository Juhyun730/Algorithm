import sys
input=sys.stdin.readline

l=[]
while 1:
    n=int(input())
    if n==0:
        break
    else:
        l.append(n)
mymax=max(l)-3
visited=[True]*(mymax+1)

'''def a(n):
    for i in range(2,int(n**(1/2))+1):
        if n % i==0:
            return False
    return True'''

for i in range(2,mymax+1):
    if visited[i]==True:
        for k in range(2*i,mymax+1,i):
            visited[k]=False


'''def mystring(x):
    s= str(x)+' = '
    for k in range(3,x):
        if a(k)==True and a(x-k)==True:
            s=s+str(k)+' + '+str(x-k)
            print(s)
            break'''

def mystring(x):
    s= str(x)+' = '
    for k in range(3,x):
        if visited[k]==True and visited[x-k]==True:
            s=s+str(k)+' + '+str(x-k)
            print(s)
            return
    print("Goldbach's conjecture is wrong.")
    return

for n in l:
    mystring(n)