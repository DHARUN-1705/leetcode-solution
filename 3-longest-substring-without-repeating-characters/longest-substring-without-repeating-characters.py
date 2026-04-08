class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        n = len(s)
        chars = set()
        max = 0
        for r in range(n):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            length = r - l + 1
            if length > max:
                max = length
        return max