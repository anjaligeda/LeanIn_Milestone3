class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_list = [0] * 101
        # count numbers
        for v in nums:
            count_list[v] += 1
        # compute numbers before current index
        for i in range(1, 101):
            count_list[i] += count_list[i-1]
        res = []
        for v in nums:
            if v == 0:
                res.append(0)
            else:
                res.append(count_list[v-1])
        return res
