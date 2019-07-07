"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入
前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        head = pre[0]
        poi = tin.index(head)
        root = TreeNode(head)
        root.left = self.reConstructBinaryTree(pre[1:poi + 1], tin[:poi])
        root.right = self.reConstructBinaryTree(pre[poi + 1:], tin[poi + 1:])
        return root


# 前序遍历
def pre_print(head_node):
    if head_node:
        print(head_node.val, end=' ')
        pre_print(head_node.left)
        pre_print(head_node.right)


# 中序遍历
def in_print(head_node):
    if head_node:
        in_print(head_node.left)
        print(head_node.val, end=' ')
        in_print(head_node.right)


# 后序遍历
def post_print(head_node):
    if head_node:
        post_print(head_node.left)
        post_print(head_node.right)
        print(head_node.val, end=' ')


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    tree = Solution()
    tree = tree.reConstructBinaryTree(pre, tin)
    pre_print(tree)
    print('\n')
    in_print(tree)
    print('\n')
    post_print(tree)
