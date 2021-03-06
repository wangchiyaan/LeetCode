# 题目描述
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

    输入: [1,2,3,4,5,6,7] 和 k = 3
    输出: [5,6,7,1,2,3,4]
    解释:
    向右旋转 1 步: [7,1,2,3,4,5,6]
    向右旋转 2 步: [6,7,1,2,3,4,5]
    向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

    输入: [-1,-100,3,99] 和 k = 2
    输出: [3,99,-1,-100]
    解释: 
    向右旋转 1 步: [99,-1,-100,3]
    向右旋转 2 步: [3,99,-1,-100]
说明:

    尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
    要求使用空间复杂度为 O(1) 的原地算法。
    
### solution 1：
依次看第一个元素：先将其pop出，再看剩余数组中是否还存在pop掉的元素。

（超出时间限制。。。）

### solution 2：
solution 1的改进：用了字典来判断是否已经存在。

（效率依然很差）

### solution 3：dict
遍历一次，利用字典存储出现次数。

### solution 4：set ^_^
利用set取数组集合，判断集合和原数组长度是否相等。

