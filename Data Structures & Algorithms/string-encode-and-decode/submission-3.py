class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string
            
    def decode(self, s: str) -> List[str]:
        str_len = ""
        res = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                str_len = int(str_len)
                res.append(s[i+1:i+str_len+1])
                i += str_len + 1
                str_len = ""
            else:
                str_len += s[i]
                i += 1
        return res