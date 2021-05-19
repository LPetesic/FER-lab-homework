from collections import deque
n,e=input().split()
info=[0]*int(n)

visited=set()
queue = deque()

for i in range(int(n)):
    temp = [-1,-1,int(input())]#[black_index,distance,type,connectedNodes]
    if(temp[2]==1) :
        queue.append((i,i,0))#(index,black_index,distance_from_black)
        visited.add(i)
    info[i]=temp
    
for i in range(int(e)):
    i1,i2=input().split()
    info[int(i1)].append(int(i2))
    info[int(i2)].append(int(i1))
info2=[z for z in info]

for i in range(10):
    n=len(queue)
    try:
        for j in range(n):
            workNode=queue.popleft()
            for k in info[workNode[0]][3:]:
                if(k not in visited):
                    queue.append((k,workNode[1],i+1))
                    visited.add(k)
            info[workNode[0]][0:2]=[workNode[1],i]
    except:
        pass
for i in range(len(info)):
    print(info[i][0],info[i][1])
