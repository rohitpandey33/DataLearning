import random
import sorting.bubble as b,sorting.insertionSort as i,sorting.selectionSort as s
seq=random.sample(range(0,100000),30000)

import cProfile
# cProfile.run('b.bubble_sort(seq)')
cProfile.run('s.selection_sort(seq)')
# cProfile.run('i.insertion_sort(seq)')
# cProfile.run('q.quick_sort(seq, 0,len(seq)-1)')
