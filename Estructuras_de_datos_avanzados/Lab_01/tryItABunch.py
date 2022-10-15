import time
from random import choice
from matplotlib import pyplot as plt


# tryItABunch: runs a function a bunch, and times how long it takes.
#
# Input: myFn: a function which takes as input a list of integers
# Output: lists nValues and tValues so that running myFn on a list of length nValues[i] took (on average over numTrials tests) time tValues[i] milliseconds.
#
# Other optional args:
#    - startN: smallest n to test
#    - endN: largest n to test
#    - stepSize: test n's in increments of stepSize between startN and endN
#    - numTrials: for each n tests, do numTrials tests and average them
#    - listMax: the input lists of length n will have values drawn uniformly at random from range(listMax)
def tryItABunch(myFn, startN=10, endN=100, stepSize=10, numTrials=20, listMax = 10):
    nValues = []
    tValues = []
    for n in range(startN, endN, stepSize):
        # run myFn several times and average to get a decent idea.
        runtime = 0
        for t in range(numTrials):
            lst = [ choice(range(listMax)) for i in range(n) ] # generate a random list of length n
            start = time.time()
            myFn( lst )
            end = time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues

# next, you can do:
# plot(nValues, tValues)
# or something like that


def copia_insertionSort(A):
  B=[None for i in range(len(A))]
  for x in A:
    for i in range(len(B)):
      if B[i]==None or B[i]>x:
        j=len(B)-1
        while j>i:
          B[j]=B[j-1]
          j-=1
        B[i]=x
        break
  return B


def InsertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A


def MergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        MergeSort(left)
        MergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array



def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A


def HeapSort(A):
    BuildMaxHeap(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        MaxHeapify(A, 0, i)

def BuildMaxHeap(A):
    for i in range(len(A)//2, -1, -1):
        MaxHeapify(A, i, len(A))

def MaxHeapify(A, i, heap_size):
    l = 2*i + 1
    r = 2*i + 2
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, largest, heap_size)


def ShellSort(A):
    n = len(A)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = A[i]
            j = i
            while j >= gap and A[j-gap] > temp:
                A[j] = A[j-gap]
                j = j-gap
            A[j] = temp
        gap = gap//2
    return A


def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        pivot = A[0]
        less = [i for i in A[1:] if i <= pivot]
        greater = [i for i in A[1:] if i > pivot]
        return QuickSort(less) + [pivot] + QuickSort(greater)


# Example usage: 50 elements
n_values_copy,t_values_copy=tryItABunch(copia_insertionSort,10,50,10,5,300)

n_values,t_values=tryItABunch(InsertionSort,10,50,10,5,300)

n_values_merge,t_values_merge=tryItABunch(MergeSort,10,50,10,5,300)

n_values_b,t_values_b=tryItABunch(BubbleSort,10,50,10,5,300)

n_values_h,t_values_h=tryItABunch(HeapSort,10,50,10,5,300)

n_values_s,t_values_s=tryItABunch(ShellSort,10,50,10,5,300)

n_values_q,t_values_q=tryItABunch(QuickSort,10,50,10,5,300)



plt.grid(True)
plt.plot(n_values_copy,t_values_copy,color='black',label='insertion+copia')
plt.plot(n_values,t_values,color='red',label='insertion')
plt.plot(n_values_merge,t_values_merge,color='blue',label='mergesort')
plt.plot(n_values_b,t_values_b,color='green',label='bubblesort')
plt.plot(n_values_h,t_values_h,color='purple',label='heapsort')
plt.plot(n_values_s,t_values_s,color='magenta',label='shellsort')
plt.plot(n_values_q,t_values_q,color='c',label='quicksort')
plt.xlabel('n')
plt.ylabel('Time')
plt.legend()
plt.show()

