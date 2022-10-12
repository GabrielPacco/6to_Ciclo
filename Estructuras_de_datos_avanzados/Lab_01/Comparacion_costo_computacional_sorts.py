import matplotlib.pyplot as plt

from tryItABunch import tryItABunch

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
  for i in range(1, len(A)):
    cur_value = A[i]
    j = i - 1
    while j >= 0 and A[j] > cur_value:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = cur_value


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

# Metodo de ordenamiento quicksort
def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        pivot = A[0]
        less = [i for i in A[1:] if i <= pivot]
        greater = [i for i in A[1:] if i > pivot]
        return QuickSort(less) + [pivot] + QuickSort(greater)




n_values_copy,t_values_copy=tryItABunch(copia_insertionSort,10,1500,10,5,300)

n_values,t_values=tryItABunch(InsertionSort,10,1500,10,5,300)

n_values_merge,t_values_merge=tryItABunch(MergeSort,10,1500,10,5,300)

n_values_b,t_values_b=tryItABunch(BubbleSort,10,1500,10,5,300)

n_values_h,t_values_h=tryItABunch(BubbleSort,10,1500,10,5,300)

n_values_sh,t_values_sh=tryItABunch(ShellSort,10,1500,10,5,300)

n_values_q,t_values_q=tryItABunch(QuickSort,10,1500,10,5,300)


plt.grid(True)
plt.plot(n_values_copy,t_values_copy,color='black',label='insertion+copia')
plt.plot(n_values,t_values,color='red',label='insertion')
plt.plot(n_values_merge,t_values_merge,color='blue',label='mergesort')
plt.plot(n_values_b,t_values_b,color='green',label='bubblesort')
plt.plot(n_values_h,t_values_h,color='purple',label='heapsort')
plt.plot(n_values_sh,t_values_sh,color='magenta',label='shellsort')
plt.plot(n_values_q,t_values_q,color='pink',label='quicksort')
plt.xlabel('n')
plt.ylabel('Time')
plt.legend()
plt.show()


if __name__ == '__main__':
    pass
