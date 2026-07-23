class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dist = {}
        for c in s:
            if c not in dist:
                dist[c] = 1
            else:
                dist[c] += 1
        
        for c in t:
            if c not in dist:
                return False
            dist[c] -= 1
            if dist[c] == 0:
                del dist[c]

        return len(dist) == 0
        
