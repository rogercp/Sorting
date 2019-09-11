# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    left = 0 
    right = 0

    for i in range(0, elements):
        if left >= len(arrA):
            merged_arr[i] = arrB[right]
            right = right + 1
        elif right >= len(arrB):
            merged_arr[i] = arrA[left]
            left = left + 1
        elif arrA[left] < arrB[right]:
            merged_arr[i] = arrA[left]
            left = left + 1
        else:
            merged_arr[i] = arrB[right]
            right = right + 1
    
    return merged_arr



my_list = [3,54,55,56,34,23,2]

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    middle_point = len(arr)//2
    left, right = merge_sort(arr[:middle_point]), merge_sort(arr[middle_point:])

    print(arr)
    return merge(left, right)


merge_sort(my_list)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
