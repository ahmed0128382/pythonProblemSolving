
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aLen = len(a)
        bLen = len(b)
        c=0
        out=""
        for i in range(abs(aLen - bLen)):
            if(aLen > bLen):
                b = "0" + b
            elif( bLen > aLen ):
                a = "0" + a
        length = len(a)        
        while( length ):
            if( a[length -1] == "1" and b[length -1] == "1" ):
                if( c == 1 ):
                    out = "1" + out
                else:
                    out = "0" + out
                c = 1
            elif( a[length -1] == "0" and b[length -1] == "1" or a[length -1] == "1" and b[length -1] == "0" ):
                if ( c == 1 ):
                    out = "0" + out
                    c = 1
                else:
                    out = "1" + out 
                    c = 0
            elif( a[length -1] == "0" and b[length -1] == "0" ):
                if ( c == 1 ):
                    out = "1" + out
                else:
                    out = "0" + out
                c = 0
            length -= 1
        if (c == 1 ):
            out = "1" + out
        return out 

solution = Solution()
sEx1 = "11"
sEx2 = "1"
print(solution.addBinary(sEx1,sEx2))