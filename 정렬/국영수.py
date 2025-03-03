n=int(input())

l=[list(input().split()) for _ in range(n)]

l.sort(key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]),(x[0])))

for i in l:
    print(i[0])