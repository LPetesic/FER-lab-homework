from sys import stdout, stdin
def iterate_Node_Rank(iter_prev,edges, edges_keys,b,n):
    residue=(1-b)/n
    iter_next=[residue]*n
    for k in edges_keys:
        result=0
        for t in edges.get(k):
            result+=iter_prev[t[0]]*t[1]
        iter_next[k]+=result*b
    return iter_next
n,b=stdin.readline().split()
n=int(n)
b=float(b)
vector_b =[round((1-b)/n,10)]*n
edges={}

for k in range(n):
    outgoing=[int(j) for j in stdin.readline().split()]
    l = 1/len(outgoing)
    for j in outgoing:
        edges[j]=edges.get(j,[])+[[k,l]]   #logika za matrice
q_number= int(stdin.readline())
queries=[]
maxx=0
for k in range(q_number):
    n_i,it=stdin.readline().split()
    if(maxx<int(it)): 
        maxx=int(it)
    queries+=[[int(n_i),int(it)]]
    
edges_keys=edges.keys()
iteration_results=[[round(1/n,10)]*n]
for i in range(maxx):
    iteration_results+=[iterate_Node_Rank(iteration_results[i],edges,edges_keys,b,n)]

for q in queries:
    stdout.write("{:.10f}\n".format(iteration_results[q[1]][q[0]]))
