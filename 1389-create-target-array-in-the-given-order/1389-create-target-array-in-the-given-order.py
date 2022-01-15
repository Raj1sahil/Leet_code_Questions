class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[]
        for i,value in zip(index, nums):
            target.insert(i,value)
        return target