class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # if sorted_s == sorted_t:
        #     return True
        # return False
        # Time complexity is O(nlogn + mlogm)

        # Hash Approach
        if len(s) != len(t):
            return False
        s_hash = {
            # letter: frequency
        }
        t_hash = {
            # letter: frequency
        }
        # generate hashmaps
        for letter in s:
            s_hash[letter] = s_hash.get(letter,0) + 1
        for letter in t:
            t_hash[letter] = t_hash.get(letter,0) + 1
        
        # check if letter and frequency match
        for letter,frequency in s_hash.items():
            if letter not in t_hash:
                return False
            if frequency != t_hash[letter]:
                return False
        return True