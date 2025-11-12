from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        
        most_common = counts.most_common(k)  
        
        return [val for val, freq in most_common]
