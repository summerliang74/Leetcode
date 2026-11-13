n = int(input())
nums = list(map(int, input().split(" ")))

nums.sort()

max_diff = float("INF")
for i in range(n-1):
    if nums[i+1] - nums[i] <= max_diff:
        max_diff = nums[i+1] - nums[i]
print(max_diff)