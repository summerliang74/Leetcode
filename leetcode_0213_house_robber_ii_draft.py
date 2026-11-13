class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        max_stollen = 0
        for start in range(len_nums-1):
            f = [0, nums[0]]
            for i in range(2, len(nums)+1):
                f_i = max(nums[i-1]+f[i-2], f[i-1])
                f.append(f_i)
                max_stollen = max(max_stollen,f[-1])
            first = nums.pop(0)
            nums.append(first)
        return max_stollen

sol = Solution()
sol.rob([2,3,2])