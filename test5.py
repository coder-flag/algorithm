# 以二叉树对应的完全二叉树为参照，空白节点处使用#字符填充，使用层次遍历表示二叉树，节点间使用空格分割，如4 2 7 # 3 6 9,
# 输出其镜像
"""
 way1 暴力美学
1.空白节点用#填充，因此可以把它当作完全二叉树
2.完全二叉树除叶节点所在层外，每层节点数满足2**n,n是所在高度高度减1，
    如第一层有2**0个节点，第二层有2**1个节点
3.计算层数
    sum = 0 ,i = 0
    循环：last_sun = sum ,sum += 2**i, i += 1
    退出循环： sum >= length
    则树的高度为 height = i，叶节点数: leaf_nodes = sum-last_sum

4.输出
    sum, count = 0, 0
    while count < height-1:
        temp = 2**count
        for i in range(temp):
            print(tree[sum+temp-1])
            temp -= 1
        sum += 2 ** count
    for end in range(leaf_nodes):
        print(tree[-(end+1)])

"""


def mirror(tree):
    if tree:
        sum, i = 0, 0
        length = len(tree)
        while sum < length:
            last_sum = sum
            sum += 2 ** i
            i += 1
        leaf_nodes = sum - last_sum
        height = i

        count_sum, count = 0, 0
        while count < height - 1:
            temp = 2 ** count
            for i in range(temp):
                print(tree[count_sum + temp - 1], end=' ')
                temp -= 1
            count_sum += 2 ** count
            count += 1
        for end in range(leaf_nodes):
            print(tree[-(end + 1)], end=' ')


if __name__ == '__main__':
    strs = input()
    strs = strs.split(' ')
    mirror(strs)
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_tree(node):



def mirror(tree):
    if tree:
        tree.left = tree.right
        tree.right = tree.left
    if tree.left:
        mirror(tree.left)
    if tree.right:
        mirror(tree.right)


"""
