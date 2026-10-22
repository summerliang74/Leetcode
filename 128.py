class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_length = 0
        if len(nums) == 1:
            return 1
        for i in nums:
            if i-1 not in nums:   
                cur = i
                tmp_length = 1
                while cur + 1 in nums:
                    tmp_length += 1
                    cur += 1
                max_length  = max(tmp_length,max_length)
        return max_length
    
sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))