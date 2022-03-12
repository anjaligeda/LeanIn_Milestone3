class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n=len(operations)
        x=0
        for i in range(0,n):
            if (operations[i]=="--X" or operations[i]=="X--"):
                x=x-1
            elif (operations[i]=="++X" or operations[i]=="X++"):
                x=x+1
            else:
                continue
            
        return x
        
