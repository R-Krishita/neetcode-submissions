class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        viewed = set()
        flag = 0
        for i in nums:
            if i not in viewed:
                viewed.add(i)
            else:
                flag = 1
        if (flag == 1):
            return True
        else:
            return False
            