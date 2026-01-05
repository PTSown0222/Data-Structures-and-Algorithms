class Solution:
    def distMoney(self, money: int, children: int) -> int:
        
        if money < children:
            return -1
        
        money -= children
        cnt = money // 7
        remaining = money % 7

        if cnt == children - 1 and remaining == 3:
            return cnt - 1
        if cnt > children or (cnt == children and remaining > 0):
            return children - 1
        
        return min(cnt, children)

