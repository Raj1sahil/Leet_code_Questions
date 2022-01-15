class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        str1=''
        for i in range(len(s)):
            for j in range(len(indices)):
                if i==indices[j]:
                    str1=str1+s[j]
        return str1