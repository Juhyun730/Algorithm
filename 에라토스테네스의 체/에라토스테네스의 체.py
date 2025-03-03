n,k=map(int,input().split())
num=0
g=[True]*(n+1)

for i in range(2,n+1):
    if g[i]==True:
        num+=1
        if num==k:
            print(i)
            break
        for t in range(i*2,n+1,i):
            if g[t]==True:
                num+=1
                #print(num,i,t,g)
                if num==k:
                    print(t)
                    break
                g[t]=False
    #print(i, g)