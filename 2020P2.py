n = int(input())
petals = list(map(int, input().split()))
cnt = 0
for start in range(n):
    currSum = petals[start]
    hashTable = set()
    hashTable.add(petals[start])
    if currSum in hashTable:
        cnt+=1
    for end in range(start + 1, n):
        hashTable.add(petals[end])
        currSum += petals[end]
        avgPetal = currSum / (end  - start + 1)
        if avgPetal in hashTable:
            cnt+=1

print(cnt)