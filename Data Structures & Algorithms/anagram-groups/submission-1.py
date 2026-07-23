class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charsToStrs = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in charsToStrs:
                charsToStrs[key].append(s)
            else:
                charsToStrs[key] = [s]

        out = []
        for v in charsToStrs.values():
            out.append(v)

        return out

