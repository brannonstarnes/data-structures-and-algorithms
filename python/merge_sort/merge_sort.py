def merge_sort(arr):
    n = len(arr)

    if n > 1:
        mid = n/2
        left = arr[0:mid]
        right = arr[mid:n]
        # sort the left side
        merge_sort(left)
        # sort the right side
        merge_sort(right)
        # merge the sorted left and right sides together
        merge(left, right, arr)

def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < left.length and j < right.length:
         if left[i] <= right[j]:
             arr[k] = left[i]
             i = i + 1
         else:
             arr[k] = right[j]
             j = j + 1

         k = k + 1

    if i == left.length:
        set remaining entries in arr to remaining values in right
    else:
        set remaining entries in arr to remaining values in left
