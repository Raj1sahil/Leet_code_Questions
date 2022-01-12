class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        f=[]
        for i in range(0,len(nums),2):
            seq,val=nums[i],nums[i+1]
            for j in range(seq):
                f.append(val)
        return f
            
            
        