# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


# 1.输入字符串
# 2.获取字符串的长度
# 3.从首字母开始遍历字符串，遇到重复字母停止，记录长度temp
# 4.从次字母开始重复以上步骤，比较两次temp大小，取大

# def get_max(strs):
#     length = len(strs)
#     temp = 0
#     for i in range(length):
#         save_char = []
#         for j in range(i, length):
#             if strs[j] in save_char:
#                 if j - i > temp:
#                     temp = j - i
#                 break
#             else:
#                 save_char.append(strs[j])
#                 if j-i+1 > temp:
#                     temp = j - i + 1
#     return temp


# 滑动窗口
def get_max(strs):
    max_len = 0
    current_len = 0
    left = 0
    length = len(strs)
    slide_window = []
    for right in range(length):
        while strs[right] in slide_window:
            slide_window.remove(slide_window[0])
            left += 1
        slide_window.append(strs[right])
        current_len = right - left + 1
        max_len = max(max_len, current_len)
    return max_len


if __name__ == '__main__':
    strs = input()
    print(get_max(strs))
