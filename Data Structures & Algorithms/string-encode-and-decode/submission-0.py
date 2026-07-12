class Solution:

    def encode(self, strs: List[str]) -> str:
        joined = ""
        for item in strs:
            joined += str(len(item))+  "#"+item
        return joined

    def decode(self, s: str) -> List[str]:
        decoded_words = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word_start = j + 1
            word_end = word_start + length

            word = s[word_start:word_end]
            decoded_words.append(word)

            i = word_end

        return decoded_words

            

            
            


