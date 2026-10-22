class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        right = 0
        left = 0
        maxlen = 0
        hashMap = {}
        while right < len(s):
            if s[right] not in hashMap:
                hashMap[s[right]] = 1
            else:
                hashMap[s[right]] += 1
        if hashMap[s[right]] >1:
            while left<=right:
                if hashMap[s[left]] == 1:
                        del hashMap[s[left]]
                        left+=1
                else:
                        hashMap[s[left]] -=1
                        left+=1

                if hashMap[s[right]] ==1:
                    break
        maxlen = max(maxlen, right - left + 1)
        right +=1
        return maxlen