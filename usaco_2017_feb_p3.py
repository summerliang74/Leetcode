import sys

sys.stdin = open("cowqueue.in", "r")
sys.stdout = open("cowqueue.out", "w")

n = int(input())
arrivalTime = []

for i in range(n):
    data = tuple(map(int,input().split()))
    arrivalTime.append(data)

arrivalTime.sort(key=lambda x: x[0])
currentTime = arrivalTime[0][0]
for i in range(n):
    startTime = max(currentTime, arrivalTime[i][0])
    currentTime=startTime + arrivalTime[i][1]


print(currentTime)
