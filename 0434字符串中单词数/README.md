# 题目描述
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

    输入: "Hello, my name is John"
    输出: 5


### solution 1：
直接计算split后的元素个数。
### solution 2：
遍历一次，只要前一个字符不是空格且后一个字符是空格就计数一个单词。