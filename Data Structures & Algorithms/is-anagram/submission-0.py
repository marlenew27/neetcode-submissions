from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_dict = defaultdict(int)
        t_char_dict = defaultdict(int)
        for c in s:
            s_char_dict[c] += 1
        for c in t:
            t_char_dict[c] += 1
        return s_char_dict == t_char_dict


        