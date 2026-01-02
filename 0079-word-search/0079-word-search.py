class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)
        # init 4-direction
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        self.found = False

        def is_word(r, c, letter):
            if not (0 <= c < cols and 0 <= r < rows):
                return False 
            if board[r][c] != letter:
                return False
            return True
        
        def TRY(i, pre_r, pre_c):
            if self.found: 
                return

            for j in range(4):

                next_r = dx[j] + pre_r
                next_c = dy[j] + pre_c

                if is_word(next_r, next_c, word[i]):
                    tmp = board[next_r][next_c]
                    board[next_r][next_c] = "1"

                    if i < n - 1:
                        TRY(i + 1, next_r, next_c)
                    else:
                        self.found = True
                
                    board[next_r][next_c] = tmp
        
        # find the first letter in this board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    tmp = board[r][c]
                    board[r][c] = "1"

                    if n == 1:
                        return True
                    else:
                        TRY(1, r, c)
                    
                    board[r][c] = tmp

                    if self.found:
                        return True
        return False


                    
