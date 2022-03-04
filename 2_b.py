#Minimum Sum of Four Digit Number After Splitting Digits
class Solution:
    def minimumSum(self, num: int) -> int:
       s2=str(num)
       N=len(s2)
       best=10**10
       for s in itertools.permutations(s2):
            s="".join(s)
            for i in range(1,N):
                left=s[:i]
                right=s[i:]
                
                best=min(best,int(left),int(right))
       return best
        
