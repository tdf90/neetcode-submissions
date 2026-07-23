from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars_to_strs = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            chars_to_strs[key].append(s)

        return list(chars_to_strs.values())


