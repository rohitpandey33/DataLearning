def bubble_sort(seq):
    n=len(seq)
    for i in range(0,n):
        for j in range(0,n-1-i):
            if seq[j]>seq[j+1]:
                temp=seq[j]
                seq[j]=seq[j+1]
                seq[j+1]=temp
    return seq

    