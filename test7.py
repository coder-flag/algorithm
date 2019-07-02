"""
给定一个中文句子s，一个中文字典文件d，其中d的每一行代表一个中文单词。
假设s是由d中的单词构成。请根据d将s切分成以空格隔开的单词序列。如果存在
多种切分方式，请输出切分后单词数目最少的一种。如果存在多种切分后单词数目
最少的方案，则随机输出一种即可。举例：s=“南京市长江大桥” d中包括“南京”、“市”、“市长”、“长江”，“大桥”，“江大桥”，
则s存在两种合法切分方式：“南京市长江大桥”和“南京市长江大桥”。鉴于后者单词个数更少，所以该种情况下应当输出后者
"""


def fib(idx):
    if (idx < 1):
        return 0

    if (idx < 3):
        return 1

    print(fib(idx - 1) + fib(idx - 2))
    return fib(idx - 1) + fib(idx - 2)


if __name__ == '__main__':
    print(fib(5))