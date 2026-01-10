class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]

        for i in range(1,numRows):
            prev_row = res[-1]
            curr_row = [1] 
            for j in range(len(prev_row) - 1):
                curr_row.append(prev_row[j] + prev_row[j+1])
            curr_row.append(1)
            res.append(curr_row)
        
        return res[:numRows]





