class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # 2. Map frequencies to buckets
        # Index represents frequency, value is a list of numbers with that frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # 3. Collect the top k elements from the right side of buckets
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        