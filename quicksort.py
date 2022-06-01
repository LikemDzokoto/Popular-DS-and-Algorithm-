def partitions(numbers ,la , hi):
    pivot = numbers[hi] #last element as pivot 
    i = la 
    for j in range(la , hi):
        if numbers[j]  < pivot:
            numbers[i] , numbers[j] = numbers[j] , numbers[i]
            i += 1 #left side of i are smaller than pivot
    numbers[i], numbers[hi] = numbers[hi], numbers[i]
    return i

def quick_sort(numbers,la,hi):
    if la < hi: 
        pivot = partitions(numbers, la,hi)
        quick_sort(numbers, la , pivot -1)
        quick_sort(numbers,  pivot+1 , hi)
    return numbers

if __name__ == "__main__":
    nums = [1, 3, 6, 7, 2, 4, 5, 8]
    print(quick_sort(nums, 0, len(nums)-1))