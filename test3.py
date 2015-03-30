def find_root(arr, i):
	if(arr[i] == i):
		return i
	return find_root(arr, arr[i])

def count_max_nodes(arr):
	for i in range(len(arr)):
		arr[i] = arr[i] - 1
	temp = {}
	for i in range(1,len(arr)):
		root = find_root(arr,i)
		if root != 0:
			temp[root] = 1

	print(len(temp))

count_max_nodes([0,0,1,2])
