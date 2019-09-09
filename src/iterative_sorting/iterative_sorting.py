# TO-DO: Complete the selection_sort() function below 

my_arr = [23,4,56,3,5]


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)-1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
    
        for j in range(cur_index,len(arr)):
            next_index = j 
            if arr[next_index] < arr[smallest_index]:
                smallest_index = next_index


        # TO-DO: swap
        a = arr[cur_index]
        arr[cur_index] = arr[smallest_index] 
        arr[smallest_index] = a

        # arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    print(arr)
    return arr

selection_sort(my_arr)

 

# TO-DO:  implement the Bubble Sort function below
my_list = [2,5,3,67,4]

def bubble_sort( arr ):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
    print(arr)
    return arr

bubble_sort(my_list)

# STRETCH: implement the Count Sort function below


# def count_sort( arr, maximum=-1 ):

#     return arr

