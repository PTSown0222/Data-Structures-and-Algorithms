class Solution:
    def splitNum(self, num: int) -> int:
        
        # small go head, big go behind

        list_num = list(str(num))
        list_num.sort()

        num1 = ""
        num2 = ""
        for i in range(len(list_num)):
            if i % 2 == 0:
                num1 += list_num[i]
            else:
                num2 += list_num[i]
        return int(num1) + int(num2)