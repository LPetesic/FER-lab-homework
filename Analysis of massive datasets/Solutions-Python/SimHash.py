import hashlib
import numpy as np
import binascii
from hexhamming import hamming_distance

def simhash(text):
    tokens = text.rstrip().lstrip().split(" ")
    sh=[0]*128
    for token in tokens:
        k=127
        hash_ = hashlib.md5(token.encode()).digest()
        for i in hash_:
            for j in range(8):
                if i & 0b00000001: 
                    sh[k]+=1
                else:
                    sh[k]-=1
                i>>=1
                k-=1
    a=np.array([1 if item>=0 else 0 for item in sh])
    simh=np.packbits(a, axis=0)
    return bytearray(simh)[::-1].hex()
N=int(input())
hashes=[]
for i in range(N):
    hashes.append(simhash(input()))
Q=int(input())
for i in range(Q):
    counter=0
    querie_index, querie_bit_tolerance=input().split(" ")
    querie_bit_tolerance=int(querie_bit_tolerance)
    querie_index=int(querie_index)
    hash_1=hashes[querie_index]
    for j in range(len(hashes)):
        if hamming_distance(hash_1,hashes[j])<=querie_bit_tolerance:
            counter+=1
    print(counter-1)
    
