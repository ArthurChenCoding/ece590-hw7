def bubbleSort_bug(arr):
    print("bubbleSort_bug is called")
    n = len(arr)
    swapped = False
    for i in range(n+1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 100]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return

def partition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def quickSort_driver(array):
    print("quickSort_driver is called")
    quickSort(array, 0, len(array) - 1)

def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)

def sort(primary_sort, alternate_sort, arr):
    try:
        o_arr = arr.copy()
        o_arr.sort()
        primary_sort(arr)
        if arr != o_arr:
            raise ValueError("wrong")
    except:
        print("failed, try alternate")
        alternate_sort(arr)


if __name__ == "__main__":
    x = [8, 2, 1, 4, 6, 2, 6, 5, 3, 7, 6, 2, 6, 5, 3, 7]
    print("erroneous version")
    sort(bubbleSort_bug, quickSort_driver, x)
    print(x)
