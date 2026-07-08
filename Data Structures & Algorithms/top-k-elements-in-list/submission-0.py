class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for item in nums:
            counter[item] = counter.get(item,0)+1
        i = k
        track =[]
        while (i>0):
            highestK=0
            highestV=0
            for key,value in counter.items():
                if value > highestV:
                    highestK = key
                    highestV = value
            track.append(highestK)
            del counter[highestK]
            i-=1
        return track