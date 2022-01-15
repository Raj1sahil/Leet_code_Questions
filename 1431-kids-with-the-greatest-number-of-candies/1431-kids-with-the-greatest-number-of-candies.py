class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        f=[]
        for i in range(len(candies)):
            flag=True
            for j in range(len(candies)):
                if candies[i]+extraCandies>=candies[j]:
                    continue
                else:
                    flag=False
                    break
            
            f.append(flag)
        return f
                    
        