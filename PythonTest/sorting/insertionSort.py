def insertion_sort(seq):
    n=len(seq)
    for i in range(0,n-1):
        if seq[i+1]<seq[i]:
            for j in range(i+1,0,-1):
                if j-1>=0 and seq[j]<seq[j-1]:    
                    temp=seq[j]
                    seq[j]=seq[j-1]
                    seq[j-1]=temp
                else:
                    break
    return seq

