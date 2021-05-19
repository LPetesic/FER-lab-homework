import math
int_list=[]
index, br_kosara, s, prag = 0, 0, 0, 0
  
br_kosara=int(input())
int_list=[0]*br_kosara
s=float(input())
prag=math.floor(s*br_kosara)
br_pretinaca=int(input())
for i in range(br_kosara):
    int_list[i]=[int(i) for i in input().split(" ")]

br_predmeta={}
for i in range(len(int_list)):
    for item in int_list[i]:
        br_predmeta[item]=br_predmeta.get(item,0)+1


pretinci=[0]*br_pretinaca

for n in int_list:
    length=len(n)
    for i in range(length):
        for j in range(length):
            if(i<j and br_predmeta[n[i]]>=prag and br_predmeta[n[j]]>=prag):
                k=(n[i]*len(br_predmeta)+n[j])%br_pretinaca
                pretinci[k]=pretinci[k]+1
rezultat={}

for n in int_list:
    length=len(n)
    for i in range(length):
        for j in range(length):
            if(i<j and br_predmeta[n[i]]>=prag and br_predmeta[n[j]]>=prag):
                k=(n[i]*len(br_predmeta)+n[j])%br_pretinaca
                if(pretinci[k]>=prag):
                    rezultat[(n[i],n[j])]=rezultat.get((n[i],n[j]),0)+1
br_cestih_apriori=len([i for i in br_predmeta.keys() if br_predmeta.get(i)>=prag])
print(int(br_cestih_apriori*(br_cestih_apriori-1)/2))
print(len(rezultat))
for item in sorted(rezultat.values(), reverse=True):
    if(item>=prag): print(item)
