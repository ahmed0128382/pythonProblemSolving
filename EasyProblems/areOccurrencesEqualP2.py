class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s_str = set(s)
        op=[]
        for i in s_str:
            c=s.count(i)
            op.append(c)
        return len(set(op))==1

solution = Solution()
st = 'aabbabccc'
print(solution.areOccurrencesEqual(st))       