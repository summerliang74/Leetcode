import sys

sys.stdin = open("triangles.in", "r")
sys.stdout = open("triangles.out", "w")

n = int(input())
coor = [tuple(map(int, input().split())) for _ in range(n)]

max_area = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):

            # 分别尝试以 i、j、k 为直角顶点
            for a, b, c in ((i, j, k), (j, i, k), (k, i, j)):
                xa, ya = coor[a]
                xb, yb = coor[b]
                xc, yc = coor[c]

                # ab 水平，ac 竖直
                if ya == yb and xa == xc:
                    area = abs(xb - xa) * abs(yc - ya)
                    max_area = max(max_area, area)

                # ab 竖直，ac 水平
                elif xa == xb and ya == yc:
                    area = abs(yb - ya) * abs(xc - xa)
                    max_area = max(max_area, area)

print(max_area)