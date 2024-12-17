class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=s.split()
        return len(x[len(x) - 1])


s = "Hello World"
solution = Solution()
result = solution.lengthOfLastWord(s)
print(result)  # Output: 5
