class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        preflen = len(pref)
        count = 0
        for i in words:
            if pref in i[:preflen]:
                count += 1
        return count
