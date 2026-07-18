
def partition(arr,low,high):
    pivot = arr[low]
    i = low + 1

    for j in range(low+1, high+1):
        if arr[j] <= pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
    arr[low],arr[i-1] = arr[i-1],arr[low]
    return i-1

def quicksort(arr,low,high):
    
    if low < high:
        p = partition(arr,low,high)
        quicksort(arr,low, p-1)
        quicksort(arr,p+1, high)

arr = [ 4,3,5,6,7,8,9,1,2]
# quicksort(arr,0, len(arr)-1)
print(arr)

def merge(left,right):
    result = []
    i=0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    # add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def mergesort(arr):
    n = len(arr)
    if n == 1:
        return arr
    mid = n//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left,right)

print(mergesort(arr))