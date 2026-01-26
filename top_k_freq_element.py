from queue import PriorityQueue


class Solution:
    def topKFrequent(nums, k):

        pq = PriorityQueue()

        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        for key, v in freq.items():
            # Use -v because pq is implemented with minheap
            # so to get highest value we need to use negative value
            # if most freq is 4, we store -4, ex: 4,3,2,1 becomes -4,-3,-2,-1
            pq.put((-v, key))

        i = 0
        res = []
        while i < k:
            res.append(pq.get()[1])
            i += 1
        return res
