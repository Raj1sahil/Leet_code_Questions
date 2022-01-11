class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_1=0
        for i in range(len(accounts)):
            sum=0
            for j in accounts[i]:
                sum=sum+j
            if sum>max_1:
                max_1=sum
        return max_1
            
        