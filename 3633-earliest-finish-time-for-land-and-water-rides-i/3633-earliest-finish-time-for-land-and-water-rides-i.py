class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        best_land_finish = float('inf')
        for start, duration in zip(landStartTime, landDuration):
            best_land_finish = min(best_land_finish, start + duration)
        
        best_water_finish = float('inf')
        for start, duration in zip(waterStartTime, waterDuration):
            best_water_finish = min(best_water_finish, start + duration)
        
        min_result = float('inf')

        for w_start, w_dur in zip(waterStartTime, waterDuration):
            start_time = max(best_land_finish, w_start)
            finish_time = start_time + w_dur
            min_result = min(min_result, finish_time)
        
        for l_start, l_dur in zip(landStartTime, landDuration):
            start_time = max(best_water_finish, l_start)
            finish_time = start_time + l_dur
            min_result = min(min_result, finish_time)
        
        return min_result
        

        return landStartTime[0] + landDuration[0] + waterStartTime[0] + waterDuration[0]

