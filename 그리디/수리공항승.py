n,l=map(int,input().split())


mysum=0

ll=list(map(int,input().split()))

ll.sort()

real_l=l-1
i=0

while i<n:
    if i<=n-2:
        start=i
        end=i+1
        if ll[end]-ll[start] <=real_l:
            while end!=n:
                now_len=ll[end]-ll[start]
                if now_len <=real_l:
                    end+=1
                    i=end
                elif now_len > real_l :
                    i=end
                    break
        else:
            i+=1
        mysum+=1
    

    elif i>n-2:
        i+=1
        mysum+=1


print(mysum)

