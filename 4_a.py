class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        N=len(nums)
        count=0
        for i in range(0,N):
            for j in nums:
                while nums[i] != 0:
                    nums[i] //= 10
                    count += 1
        return nums[i]
            
         
