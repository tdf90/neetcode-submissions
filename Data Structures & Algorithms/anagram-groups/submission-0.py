class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charsToStrs = {}
        for s in strs:
            chars = "".join(sorted(s))
            if chars in charsToStrs:
                charsToStrs[chars] += [s]
            else:
                charsToStrs[chars] = [s]

        out = []
        for v in charsToStrs.values():
            out += [v]

        return out

