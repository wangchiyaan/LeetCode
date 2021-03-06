class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        import collections
        l = len(p)
        res = []
        for i in range(len(s)):
            temp = s[i:i + l]
            if collections.Counter(list(p)) == collections.Counter(list(temp)):
                res.append(i)
        return res


if __name__ == "__main__":
    x = "cbaebabacd"
    y = "abc"
    print(Solution().findAnagrams(x, y))
