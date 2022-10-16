def bubble_sort(arr, ascending=True):
    """
    My version of the Bubblesort Algorithm 
    (No comments, hopefully self explanatory)
    
    Args:
        arr(list):       The integer array to be sorted
        ascending(bool): True for ascending order and
                         False for descending order

    Returns:
        arr(list):      The sorted integer array

    """
    for i in range(len(arr)):
        for i in range(1, len(arr)):
            if ascending and arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
            elif not ascending and arr[i-1] < arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
            else: continue
    return arr
