# Hint 3
# We can use an encoding approach where we start with a number 
# representing the length of the string,
#  followed by a separator character (let's use # for simplicity),
#  and then the string itself. To decode, we read the number until we reach a #, 
# then use that number to read the specified number of characters as the string. 

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for word in strs:
            #length of str + delimiter(#)
            header = str(len(word)) + "#" + word
            encoded_str+= header
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []

        i = 0
        while i < len(s):
            count = ""
            while s[i]!= "#":
                count+=s[i]
                i+=1
            decoded_str.append(s[i+1 : i+int(count)+1])
            i+= int(count) + 1
        return decoded_str


