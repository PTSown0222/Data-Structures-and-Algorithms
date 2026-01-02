class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # # trucksize = 10
        # max = 5 * 10 + 9 * 3 + 2 * 7 = 50 + 27 + 14 = 91

        boxTypes.sort(key = lambda x: x[1], reverse = True)
        total_units = 0

        for num_boxes, unit_per_box in boxTypes:
            if truckSize > num_boxes:
                total_units += num_boxes * unit_per_box
                truckSize -= num_boxes
            else:
                total_units += truckSize * unit_per_box
                return total_units
        
        return total_units
                
