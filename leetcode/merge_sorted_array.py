def merge_sorted_array(nums1, nums2, m, n): 
    x, y, z = 0

    while y < n:
        if nums1[x] <= nums2[y]:
            x += 1 
        else:
            temp = nums1[x]
            nums1[x] = nums2[y]
            nums1[m] = temp
            y += 1 
            m += 1
            import pdb; pdb.set_trace()


merge_sorted_array([])