class Solution:
    def maxProductDifference(self, nums):
        
        return (sorted(nums)[-1]*sorted(nums)[-2])-(sorted(nums)[0]*sorted(nums)[1])
    
