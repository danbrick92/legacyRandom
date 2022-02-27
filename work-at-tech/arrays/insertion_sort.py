class Solution:
	def insertionSort(self, arr: List[int]) -> List[int]:
		arr_size = len(arr)
		for i in range(arr_size):
			val = arr[i]
			smallest = i
			# Check rest of array to find smallest value
			for j in range(i+1, arr_size):
				if arr[j] < arr[smallest]:
					smallest = j
			# Swap smallest and current values
			arr[i] = arr[smallest]
			arr[smallest] = val
		return arr
