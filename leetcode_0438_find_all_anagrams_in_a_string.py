class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_s = len(s)
        len_p = len(p)
        p_count = {}
        ans = []
        s_count = {}

        # If the length of p is greater than the length of s, return an empty list
        if len(s)< len(p):
            return ans 
        # Count the frequency of each character in p
        for char in range(len_p):
            if p[char] not in p_count.keys():
                p_count[p[char]] = 1
                continue
            p_count[p[char]]+=1

        # Count the frequency of each character in the first window of s
        for i in range(0, len_p):
            if s[i] not in s_count.keys():
                s_count[s[i]] = 1
                continue
            s_count[s[i]] += 1
        
        #Check for illegal cases
        if s_count == p_count:
            ans.append(0)

        if len_s == len_p:
            return ans
        
        for right in range(len_p, len_s):
            left  = right - len_p
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
            if s[right] not in s_count.keys():
                s_count[s[right]] = 1
            else:
                s_count[s[right]] += 1

            if s_count == p_count:
                ans.append(left + 1)
        return ans


sol = Solution()
s = "cbaebabacd"
p = "abc"
print(sol.findAnagrams(s, p))