class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        n=len(sentence)
        if len(set('abcdefghijklmnopqrstuvwxyz') - set(sentence.lower())) == 0 :
            return True

        return False
  
