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
        
        