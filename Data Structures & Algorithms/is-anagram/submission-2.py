class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_cnt = [0] * 26
        for i in range(len(s)):
            char_cnt[ord(s[i])-ord('a')] += 1
            char_cnt[ord(t[i])-ord('a')] -= 1
        return all(c==0 for c in char_cnt)


        