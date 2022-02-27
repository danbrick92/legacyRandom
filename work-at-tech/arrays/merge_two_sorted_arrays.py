class Solution:
	def mergeSortedArrays(self, A: List[int], B: List[int]) -> List[int]:
		arr_merged = []
		ind_a = 0
		ind_b = 0
		arr_size = len(A) + len(B)
		compare_a = True
		compare_b = True
		for i in range(arr_size):
			# Check if exceeded array sizes
			if not compare_a:
				arr_merged.append(B[ind_b])
				ind_b += 1
			elif not compare_b:
				arr_merged.append(A[ind_a])
				ind_a += 1
			# The list element in A is smaller
			elif (A[ind_a] <= B[ind_b]):
				arr_merged.append(A[ind_a])
				ind_a += 1
				if (ind_a >= len(A)):
					compare_a = False
			# The list element in B is smaller
			elif (A[ind_a] > B[ind_b]):
				arr_merged.append(B[ind_b])
				ind_b += 1
				if (ind_b >= len(B)):
					compare_b = False
		return arr_merged
