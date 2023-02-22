class Solution(object):
    
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
  
