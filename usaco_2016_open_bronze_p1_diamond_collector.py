n, k = tuple(map(int, input().split()))

size = []
for i in range(n):
    size.append(int(input()))

size.sort()

cnt = 0
left = 0
right = 0

maxLength = 0
while right < n:
    if size[right] - size[left] <= k:
        maxLength = max(maxLength, right - left + 1)
    else:
        while left<=right:
            left+=1
            if size[right] - size[left] <=k:
                maxLength = max(maxLength, right - left + 1)
                break
    right += 1
print(maxLength)