class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s)) + "/" + s + "/"
        return out
             
    def decode(self, s: str) -> List[str]:
        substr = ""
        strs = []

        i = 0
        while i < len(s):
            c = s[i]
            if c.isnumeric():
                substr += c

            if s[i] == "/":
                l = int(substr)
                this = s[i+1:i+l+1]
                strs.append(this)

                substr = ""
                i += l + 2
                continue

            i += 1
        
        return strs
                
                

