class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        f=[]
        for i in range(2):
            f.extend(nums)
        return f
        