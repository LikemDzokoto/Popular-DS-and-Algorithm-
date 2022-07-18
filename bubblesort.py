def BubbleSort(arr):
    n = len(arr)

#traverse through all the elements in the array
    for i in range(n-1):
        #optimised check for checking if the swap has occurred
        swapped = False 

        #inner loop to compare all the elements in the array
        #traverse the array from 0 to n-i-1
        for j in range(0, n-i-1):
            #swap if the element found is greater than the next element 
            if arr[j] > arr[j + 1]:
                
                #swapping takes place 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break 
                #stop the iteration if the array is already swapped 
    
            
    return arr 
    #array sample to be tested 
arr = [64, 34, 25, 12, 22, 11, 90]
result = BubbleSort(arr)
print(result)