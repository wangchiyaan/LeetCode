# 题目描述
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

        输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。
说明:所有输入只包含小写字母 a-z 。

### solution 1：
以第一个字符串str[0]为比较，如果其他字符串的第一个字符与str[0]的第一个字符相同，则继续比较下一个字符；
否则比较完毕。
### solution 2：
利用python的max()和min()，在Python里字符串是可以比较的，按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
