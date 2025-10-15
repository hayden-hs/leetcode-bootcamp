class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new = s.split()
        l = 0
        r = len(new) -1
        while r > l:
            new = self.swap(new, l, r)
            l += 1
            r -=1
        output = " ".join(new)
        return output
        
    
    def swap(self, arr, l, r):
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
        return arr