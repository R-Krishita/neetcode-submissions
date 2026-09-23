class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_cpy = ""
        for char in s.lower():
            if(char.isalnum()):
                str_cpy+=char
        print(str_cpy)
        reverse = str_cpy[::-1]
        print(reverse)
        if (reverse == str_cpy):
            return True
        else:
            return False
