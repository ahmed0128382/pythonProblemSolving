class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


solution = Solution()

needle = "ahm"
haystack = "my name is ahmed"
print(solution.strStr(haystack,needle))