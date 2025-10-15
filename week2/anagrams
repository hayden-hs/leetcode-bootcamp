class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(p) > len(s):
            return []

        k = len(p)
        need, window = {}, {}

        for ch in p:
            need[ch] = need.get(ch, 0) + 1
        for ch in s[:k]:
            window[ch] = window.get(ch, 0) + 1

        out = []
        if window == need:
            out.append(0)

        for r in range(k, len(s)):
            add = s[r]
            window[add] = window.get(add, 0) + 1

            rem = s[r - k]
            window[rem] -= 1
            if window[rem] == 0:
                del window[rem]

            if window == need:
                out.append(r - k + 1)
        return out
