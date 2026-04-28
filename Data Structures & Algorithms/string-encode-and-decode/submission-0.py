class Solution:

    def encode(self, strs: List[str]) -> str:
        # "int#stringint#string"
        result = "".join(f"{len(s)}#{s}" for s in strs)
        return result
        

    def decode(self, s: str) -> List[str]:
        result = []
        word_pointer = 0
        # "5#hello5#world"
        while word_pointer < len(s):
            # remaining string
            rem_str = s[word_pointer:]
            word_length = rem_str.split('#')[0]
            word = rem_str[len(word_length)+1:len(word_length)+1+int(word_length)]
            result.append(word)

            word_pointer += len(word_length)+1+int(word_length)
        return result
