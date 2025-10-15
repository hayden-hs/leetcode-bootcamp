class Solution(object):
    def myAtoi(self, s):
        i, n = 0, len(s)
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        
        sign = 1
        if s[i] in ('+', '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        out = 0
        while i < n and s[i].isdigit():
            d = ord(s[i]) - ord('0')
            if out > (INT_MAX - d) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            out = out * 10 + d
            i += 1

        return sign * out
