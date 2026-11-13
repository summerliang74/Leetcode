import sys

sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")
    

n,m = map(int, input().split())
plain = []
spotty = []
for _ in range(n):
    spotty.append(input())
for _ in range(n):
    plain.append(input())
cnt = 0
for i in range(m):
    spotty_set = set()
    for j in range(n):
        spotty_set.add(spotty[j][i])
    for j in range(n):
        if plain[j][i] in spotty_set:
            break
    else:
        cnt += 1
print(cnt)
    