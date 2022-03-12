class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n=len(nums)
        prod=1
        for i in range(n):
            prod*=nums[i]
        if prod>0:
            return 1
        elif prod==0:
            return 0
        else:
            return -1
