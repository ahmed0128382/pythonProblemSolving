from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        min_len = min(len(s) for s in strs)
        
        for i in range(min_len):
            current_char = strs[0][i]
            if all(s[i] == current_char for s in strs[1:]):
                res+= current_char
            else:
                break
        return res

# Example usage:
str1 = ["flower","flow","flight"]
solution = Solution()
result = solution.longestCommonPrefix(str1)
print(result)  # Output: "fl"