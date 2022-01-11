class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first=nums[:n]
        second=nums[n:]
        f=[]
        for i in range(len(first)):
            f.append(first[i])
            f.append(second[i])
            
        return f
            
        
        
        