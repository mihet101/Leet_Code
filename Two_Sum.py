class Solution(object):
    
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):         
            x = nums[i]
            y = target - nums[i]
            if (y == nums[i]):              #check if we have n+n = target
                if (y in nums[(i+1):]):
                    y_index = (nums[(i+1):].index(y) + (i+1)) 
                    x_index = nums.index(x)
                    return[x_index, y_index]   
            else:                           #is m+n = target  
                if (y in nums):
                    y_index = nums.index(y)
                    x_index = nums.index(x)
                    return[x_index, y_index]


class betterSolution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}  #create hash map
        
        for i, n in enumerate(nums):  #enum the given list with index i and value n
            diff = target - n
            if diff in prevMap: #if the difference already exists in the map then return it
                return[prevMap[diff], i]
            prevMap[n] = i    #if not then add it to the hash map
        return
