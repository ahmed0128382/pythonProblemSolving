class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack.split()
        print(haystack)
        return haystack.find(needle)


solution = Solution()

needle = "sad"
haystack = "sabutsad"
print(solution.strStr(haystack,needle))