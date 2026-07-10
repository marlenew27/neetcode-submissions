class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        min_heap = []
        for n, freq in count.items():
            heapq.heappush(min_heap,(freq,n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        result = []
        for i in range(k):
            result.append(heapq.heappop(min_heap)[1]) 
        return result       
        