class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            str_len = len(s) 
            encoded_string += str(str_len) + "#" + s
    
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            i = j + 1 + length
        return res