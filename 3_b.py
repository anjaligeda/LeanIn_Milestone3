class Solution:
    def sumOfUnique(self, nums):
        ans=[]
        for i in nums:
            if nums.count(i)==1:
                ans.append(i)
                
        
        return sum(ans)
