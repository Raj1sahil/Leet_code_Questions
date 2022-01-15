class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        d=first
        ans=[]
        ans.append(first)
        for i in range(len(encoded)):
            ans.append(encoded[i] ^ d)
            d = encoded[i] ^ d
        return ans
            
        
            
        