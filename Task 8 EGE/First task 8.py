from itertools import*
index=0
for i in product(sorted("УЦЮТПСОШ"), repeat=6):
    string=''.join(i)
    index+=1
    if string=="ЮШОССО":
        print(index)
        break