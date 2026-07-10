class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            char_dict[tuple(count)].append(s)
        return [val for val in char_dict.values()]