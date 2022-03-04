#Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        N=len(nums)
        a=[nums[0]]
        for i in range(1,N):
            nums[i]+=nums[i-1]
            a.append(nums[i])
        return a
