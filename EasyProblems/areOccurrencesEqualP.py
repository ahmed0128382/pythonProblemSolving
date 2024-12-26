class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        arr = {} 
        equal = True
        cmp = 0
        for ch in s :
            if ch in arr :
                arr[ch] +=1
            else :
                arr[ch] = 1 
        cmp = arr[s[0]]
        for k in arr :
            if arr[k] != cmp :
                return False
        return equal

            
solution = Solution()
st = 'aabbabcc'
print(solution.areOccurrencesEqual(st))