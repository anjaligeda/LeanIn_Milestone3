#Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        productTotal=1
        SumTotal=0
        numbers=str(n)
        for i in numbers:
            productTotal *=int(i)
            SumTotal +=int(i)
        return productTotal - SumTotal
