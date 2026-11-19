n = int(input())
nums = list(map(int, input().split()))

group1 = []
group2 = []
diff = []
def dfs(i):
    if i == n:
        diff.append(abs(sum(group1)-sum(group2)))
        return

    group1.append(nums[i])
    dfs(i+1)

    group1.pop()
    group2.append(nums[i])
    dfs(i+1)
    group2.pop()

dfs(0)
print(min(diff))