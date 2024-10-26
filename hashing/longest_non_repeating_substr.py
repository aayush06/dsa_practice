"""
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

"""

def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    seen = {}
    max_length = 0
    for right, value in enumerate(s):
        if value in seen:
            left = max(left, seen[value]+1)
        max_length = max(max_length, right-left+1)
        seen[value] = right
    return max_length

s = "pwwkew"
solution = lengthOfLongestSubstring(s)
print(solution)
