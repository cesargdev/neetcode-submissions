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
        for i in range(len(s)):
            s_hash[s[i]] = s_hash.get(s[i],0) + 1
            t_hash[t[i]] = t_hash.get(t[i],0) + 1
        # if equal, anagram exists
        return s_hash == t_hash