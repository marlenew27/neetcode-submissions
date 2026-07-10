class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_dict = defaultdict(list)
        if len(strs) == 1:
            return [strs]
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            char_dict[tuple(count)].append(s)
        return list(char_dict.values())