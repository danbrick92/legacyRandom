class Solution:
	def twoSum(self, A: List[int], target: int) -> List[int]:
		arr_size = len(A)
		map_val = {}
		for i in range(arr_size):
			x = A[i]
			sub = target-x
			y = map_val.get(sub)
			if (y is not None):
				return [i, y]
			map_val[x] = i
		raise Exception("TargetNotPossible")
