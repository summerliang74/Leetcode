class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[1 for i in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = path[i-1][j] + path[i][j-1]
                print(path)
        return path[-1][-1] 

sol = Solution()
sol.uniquePaths(3, 7)