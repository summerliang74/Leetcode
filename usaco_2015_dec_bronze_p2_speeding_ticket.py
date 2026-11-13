import sys

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

inh = input().split()
n = int(inh[0])
m = int(inh[1])
seg = []
max_diff = 0
for i in range(n):
    inh = input().split()
    for i in range(int(inh[0])):
        seg.append(int(inh[1]))
idx=0
for i in range(m):
    inh = input().split()
    l = int(inh[0])
    r = int(inh[1])
    for j in range(l):
        max_diff = max(max_diff, (r-seg[idx]))
        idx+=1
print(max_diff)