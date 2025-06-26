from collections import Counter


class Solution:
    #  Approach 1
    #     count how many times each character appears in s using a hashmap.

    # Loop through characters in t, and for each:

    #     Check if it's in the hashmap.

    #     If not, or if its count is already 0, return False.

    #     Otherwise, decrement the count in the hashmap.

    # At the end, check that all values in the hashmap are zero — meaning all characters matched.

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}

        for char in s:
            s_map[char] = s_map.get(char, 0) + 1

        for char in t:
            if char not in s_map or s_map[char] == 0:
                return False
            s_map[char] -= 1

        return True

    # Time complexity O(n) where n is the length of the string
    #  Space complexity: O(1) there are at most 26 letters for lowercase input, but the inut size is still fixed/constant, therefor O(1) space is used

    #  Approach 2 ( troll approach, more efficient)

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
