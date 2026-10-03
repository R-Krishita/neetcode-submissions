class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str=''
        min_len=min(len(word1),len(word2))
        for i,j in zip(word1,word2):
            str+=i
            str+=j
        if(len(word1)<len(word2)):
            str+=word2[min_len:]
        else:
            str+=word1[min_len:]
        return str