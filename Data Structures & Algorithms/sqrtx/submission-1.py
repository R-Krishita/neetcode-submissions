class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = max(1,x)
        if(x == 1):
            return 1
        for _ in range(100):
            mid = (low+high)//2
            if((mid*mid) > x):
                high = mid
            else:
                low = mid
        return low