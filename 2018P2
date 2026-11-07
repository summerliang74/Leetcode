import sys

sys.stdin = open("lifeguards.in", "r")
sys.stdout = open("lifeguards.out", "w")

n = int(input())
lis = [0 for i in range(1000)]
max_time = 0
employees = []
for i in range(n): 
    imh = input().split()
    start, end = int(imh[0]), int(imh[1])
    employees.append((start, end))
    for idx in range(start, end):
        lis[idx]+=1

for i in range(n):
    start, end = employees[i]
    for idx in range(start, end):
        lis[idx]-=1
    time = 1000-lis.count(0)
    max_time = max(max_time, time)
    for idx in range(start, end):
        lis[idx]+=1

print(max_time)