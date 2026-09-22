class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_set = set()
        # t_set = set()
        # for i,j in zip(s,t):
        #     s_set.add(i)
        #     t_set.add(j)
        # if (s_set == t_set):
        #     return True
        # else:
        #     return False
        return sorted(s) == sorted(t)
        
            
        