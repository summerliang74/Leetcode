nums = list(map(int, input().split()))

nums.sort()
c = nums[6] - nums[1] - nums[0]
print(nums[0],nums[1],c )
