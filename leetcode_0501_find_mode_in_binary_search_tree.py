# ================= 1. 树节点的定义 =================
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ================= 2. 构建树的辅助函数 =================
# 按照 LeetCode 的层序遍历数组格式构建二叉树
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        curr = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1
    return root

class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        dic = {}
        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            dic[node.val] = dic.get(node.val, 0) + 1
            dfs(node.right)
        dfs(root)
        return [k for k, v in dic.items() if v == max(dic.values())]
    
if __name__ == "__main__":
    # 测试用例 1 (LeetCode 示例): root = [1,null,2,2]
    # 注意：这里的 2,2 表示 2 的左节点为空，右节点为 2
    # 实际树结构：
    #   1
    #    \
    #     2
    #    /
    #   2
    test_input = [1, None, 2, 2]
    root = build_tree(test_input)
    
    solution = Solution()
    result = solution.findMode(root)
    print("测试用例 1 结果:", result)  # 应该输出: [2]

    # 测试用例 2: root = [0]
    root2 = build_tree([0])
    result2 = solution.findMode(root2)
    print("测试用例 2 结果:", result2) # 应该输出: [0]