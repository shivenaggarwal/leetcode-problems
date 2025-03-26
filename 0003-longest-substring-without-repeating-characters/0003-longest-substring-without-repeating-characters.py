class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        longest = 0
        unique = set()

        for r in range (len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l+=1

            longest = max(longest, (r-l) + 1)
            unique.add(s[r])

        return longest
        