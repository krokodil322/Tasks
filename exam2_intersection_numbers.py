nums1 = {int(num) for num in input().split()}
nums2 = {int(num) for num in input().split()}

if len(nums1.intersection(nums2)) != 0:
	print(*sorted(nums1.intersection(nums2), reverse=True))
else:
	print("BAD DAY")