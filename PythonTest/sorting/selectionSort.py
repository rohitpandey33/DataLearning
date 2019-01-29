#find min of remaining array element and add that min to the already sorted part of the array
def selection_sort(seq):
    n=len(seq)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if seq[min_index]>seq[j]:
                min_index=j
        #swap if min index changed
        if min_index!=i:
            temp=seq[i]
            seq[i]=seq[min_index]
            seq[min_index]=temp
    return seq 
