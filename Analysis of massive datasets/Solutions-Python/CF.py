from decimal import Decimal, ROUND_HALF_UP
import numpy as np

def cosine_dist(a,b):
    return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))

def querie(i,j,k,matrix,matrix_original): #matrix moze biti item-item ili user-user
                          #ako je item-item sve normalno
                          #inače, predaj zamijenjeni i,j
    simil=[]
    for q in range(len(matrix)):
        if(q!=i and matrix_original[q][j]!=0): #matrix je vec oduzeto, moras provjeriti jel u originalnoj matrici 0
            simil.append([q,cosine_dist(matrix[q],matrix[i])])
            
    simil.sort(reverse=True, key= lambda x: x[1])
    if(len(simil)==0): return 0;
    if(k>len(simil)): k=len(simil)
    
    summ=0
    simil_summ=0
    for i in range(k):
        if(simil[i][1]>0):
            summ+=simil[i][1]*matrix_original[simil[i][0]][j]
            simil_summ+=simil[i][1]
        else:
            break
    return Decimal(Decimal(summ/simil_summ).quantize(Decimal('.001'), rounding=ROUND_HALF_UP))

dimensions = input().split()
N = int(dimensions[0])
M = int(dimensions[1])
matrix = []
queries =[]
for i in range(N):
    matrix.append([int(i) if(i!="X") else 0 for i in input().split()])
Q = int(input())
for i in range(Q):
    queries.append([int(i) for i in input().split()])


item_item_matrix=[0]*N
user_user_matrix=[0]*M


for i in range(N):
    avg=sum(matrix[i])/(M-matrix[i].count(0))
    item_item_matrix[i]=[k-avg if k!=0 else 0 for k in matrix[i]]
matrix2=list(map(list, zip(*matrix))) #evil transpose hack
for i in range(M):
    avg=sum(matrix2[i])/(N-matrix2[i].count(0))
    user_user_matrix[i]=[k-avg if k!=0 else 0 for k in matrix2[i]]
    
result=[] 
for q in queries:
    if (q[2]==0):
        print(querie(q[0]-1,q[1]-1,q[3],item_item_matrix,matrix))
    else:
        print(querie(q[1]-1,q[0]-1,q[3],user_user_matrix,matrix2))
