class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        encounters = {}
        start = 0
        longestString = ""
        currentString = ""

        for index, char in enumerate(s):
            if char in encounters and encounters[char] >= start:
                start = encounters[char]
                currentString = s[encounters[char] + 1: index + 1]
            else:
                currentString += char
            encounters[char] = index

            if len(longestString) < len(currentString):
                longestString = currentString

        return len(longestString)
