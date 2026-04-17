class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1.sort()
        # nums2.sort()
        n = len(nums1)
        m = len(nums2)
        intersect = []
        # i = 0
        # j = 0
        # while i < n and j < m:
        #     if nums1[i] == nums2[j]:
        #         intersect.append(nums1[i])
        #         i+=1
        #         j+=1
        #     elif nums1[i] < nums2[j]:
        #         i+=1
        #     else:
        #         j+=1
        # return intersect

        # way2 : hashmap
        # idea: đếm tần suất nums1 tạo thành 1 lookup table
        # iterate qua nums2 sau đó retrieve về nums1 xem có giống nhau không
        # nums1: {2:2}
        if n > m:
            return self.intersect(nums2,nums1)
        cnt = Counter(nums1)
        
        for i in nums2:
            if cnt[i] > 0:# có xuất hiện ở cả 2 mảng
                intersect.append(i)
                cnt[i] -= 1
        return intersect

            