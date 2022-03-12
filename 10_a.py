class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_balue = 0
        ind_value = 0
        for i in range(len(accounts)):
            ind_value = sum(accounts[i])
            if ind_value > max_balue:
                max_balue = ind_value
        return max_balue
