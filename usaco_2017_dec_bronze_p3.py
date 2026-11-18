import sys

sys.stdin = open("measurement.in", "r")
sys.stdout = open("measurement.out", "w")

n = int(input())
datas = []
cnt = 0
milk = {"bessie":7, "elsie":7, "mildred":7}
previousLeaders = {"bessie", "elsie", "mildred"}
for i in range(n):
    data = list(input().split())
    data[0] = int(data[0])
    data[1] = data[1].lower()
    data[2] = -int(data[2][1:]) if data[2][0] == "-" else int(data[2][1:])
    datas.append(data)
datas.sort(key = lambda x: x[0])

for day in range(n):
    cow = datas[day][1]
    milk[cow] += datas[day][2]
    maxMilk = max(milk.values())
    currentLeaders = set()
    for name, amount in (milk.items()):
        if amount==maxMilk:
            currentLeaders.add(name)
    if currentLeaders != previousLeaders:
        previousLeaders = currentLeaders
        cnt+=1
print(cnt)