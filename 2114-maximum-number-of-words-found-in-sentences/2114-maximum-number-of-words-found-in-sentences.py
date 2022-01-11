class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_value=0
        for i in range(len(sentences)):
            count=0
            for j in sentences[i].split():
                count=count+1
            if count>max_value:
                max_value=count
        return max_value
            
            
        