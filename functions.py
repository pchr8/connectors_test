import numpy as np
import random
def generate_names(num):
    n=np.load('./static/last.npy');

    # List of decreasing integers
    weights=list(range(len(n), 0, -1))
    sum=0
    for i in weights:
        sum+=i
    # So that they sum up to 1
    pweights=[]
    for i in weights:
        pweights.append(i/sum)
    
    n1=np.random.choice(n, size=num, p=pweights)
    n2=np.random.choice(n, size=num)
    return n1, n2


