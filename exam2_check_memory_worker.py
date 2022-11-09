nums1, nums2 = {int(num) for num in input().split()}, {int(num) for num in input().split()}
print("YES" if len(nums1.intersection(nums2)) == len(nums1) and len(nums2.difference(nums1)) == 0 else "NO" )

