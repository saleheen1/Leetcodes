class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        countHash = {}
        freqBucket = [[] for i in range(len(nums) +1)]
        
        
        for v in nums:
            countHash[v] = countHash.get(v,0) + 1

        for key,value in countHash.items():
            freqBucket[value].append(key)

        result = []
        for i in reversed(range(len(freqBucket))):
            for f in freqBucket[i]:
                result.append(f)
                if len(result) == k:
                    return result

        

        




s =Solution()
print(s.topKFrequent(nums=[1,1,1,3,3,3,2,2],k=3))