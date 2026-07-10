from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_dict = defaultdict(int)
        for c in s:
            char_dict[c] += 1
        for c in t:
            char_dict[c] -= 1
        return len(set(char_dict.values())) == 1


        