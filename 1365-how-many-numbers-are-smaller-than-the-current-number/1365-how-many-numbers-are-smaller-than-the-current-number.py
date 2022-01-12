class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        f=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if i==j:
                    continue
                elif nums[i]>nums[j]:
                    # print("nums of i is ",nums[i])
                    count=count+1
                
            f.append(count)
        return f
        
        