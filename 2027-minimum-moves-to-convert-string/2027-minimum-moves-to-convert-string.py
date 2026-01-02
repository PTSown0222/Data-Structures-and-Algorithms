class Solution:
    def minimumMoves(self, s: str) -> int:
        move = 0
        i = 0
        while i < len(s):
            if s[i] == 'X':
                i+=3
                move+=1
            else:
                i += 1
        return move