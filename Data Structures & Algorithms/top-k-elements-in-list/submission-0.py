class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {
            # number:frequency
        }
        result = []
        # create frequency count
        for number in nums:
            freq_count[number] = freq_count.get(number,0)+1
        
        # create bucket array with length of nums + 1
        # index is the frequency, value is a list of numbers with that frequency
        bucket_array = [[] for _ in range(len(nums)+1)]

        for number,count in freq_count.items():
            bucket_array[count].append(number)
        for i in range(len(nums),0,-1):
            for number in bucket_array[i]:
                result.append(number)
                if len(result) == k:
                    return result
                    