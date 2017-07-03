def mergeSort(arr1, m, arr2, n):
    while m > 0 and n > 0:
        if arr1[m-1] >= arr2[n-1]:
            arr1[m+n-1] = arr1[m-1]
            m -= 1
        else:
            arr1[m+n-1] = arr2[n-1]
            n -= 1
        print arr1
    if n > 0:
        arr1[:n] = arr2[:n]

arr1 = [2,4,6,8]
arr2 = [1,3,5,7]

m = len(arr1)
n = len(arr2)

for i in range(n):
    arr1.append(0)
#print arr1

# Modify the aray here to change the length
mergeSort(arr1, m , arr2, n)
print arr1