n = int(input())
s = input()

ans = 0
# 枚举起点
for i in range(n):
    g_count = 0
    h_count = 0
    # 枚举终点
    for j in range(i, n):
        if s[j] == 'G': g_count += 1
        else: h_count += 1
        
        # 如果区间长度 >= 3 且 (只有1个G 或 只有1个H)
        if j - i + 1 >= 3:
            if g_count == 1 or h_count == 1:
                ans += 1

print(ans)