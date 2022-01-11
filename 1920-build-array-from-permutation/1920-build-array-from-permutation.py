class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        f=[]
        for i in range(len(nums)):
            f.append(nums[nums[i]])
        return f
        