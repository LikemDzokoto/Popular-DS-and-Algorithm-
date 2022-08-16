 
class Search(object):
    def search(self, nums, target):
        i,j =0 , len(nums) -1 
        while i <= j:
            middle = (i +j)//2
            if nums[middle] ==target:
                return middle
            elif nums[middle] > target:
                j = middle -1 
            else:
                i = middle + 1
        return -1     

def binary_search(my_list, item):
    low = 0
    high = len(my_list) -1
    
    while low <= high:
        mid = round((low + high)/2)
        guess = my_list[mid]

        if guess == item:
            return guess
        if guess > item: #The guess was too high
            high = mid -1
        else: # The guess was too low
            low = mid + 1
    return None
        


my_list = [1, 3, 5, 7, 9] 
print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1))# =>  None
