n,m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

chosen = []
count = 0
total = 0
def recursion(i,total):
    global count
    if i == n:
        if total == m:
            count+=1
        return

    chosen.append(nums[i])
    recursion(i+1,total+nums[i])

    chosen.pop()

    recursion(i+1, total)

recursion(0,total)
print(count)