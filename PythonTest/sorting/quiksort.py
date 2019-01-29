def partition(seq,high,low):
    pindex=low+1
    pivot=seq[low]
   
    for i in range(low,high+1):
        if  seq[i]<pivot:
            temp=seq[pindex]
            seq[pindex]=seq[i]
            seq[i]=temp
            pindex+=1
    #swap pivot and pindex
    seq[low]=seq[pindex-1]
    seq[pindex-1]=pivot
    return pindex-1
def quick_sort(seq,low,high):
    if low>=high:
        return
    else:
        pindex=partition(seq, high, low)
        quick_sort(seq,low,pindex-1)
        quick_sort(seq,pindex+1,high)
    return seq


# import cProfile,random
# seq=random.sample(range(0,1000000),100000)
# 
# cProfile.run('quick_sort(seq,0,len(seq)-1)  ')