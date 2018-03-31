print ('Sorting')
def selectionSort(aList):
    for i in range(len(aList)):
        least = i
        for k in range(i+1, len(aList)):
            if aList[k] < aList[least]:
                least = k
                 
        swap(aList, least, i)
         
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

my_list = [55.32,13.12,1.84,35.64,5.66,88,101.1,8.97,4.12,36.28,43.5]
selectionSort(my_list)
print (my_list)


print ('Searching')
def binary_search(number, target):
    low = 0
    mid = len(number) / 2
    upper = len(number)

    if len(number) == 1:
        if number[0] == target:
            print target
            return number[0]
        else:
            return False
    if target == number[mid]:
        print number[mid]
        return mid
    else:
        if mid > low:
            numberl = number[0:mid]
            binary_search(numberl, target)

        if upper > mid:
            number2 = number[mid:len(number)]
            binary_search(number2, target)

if __name__ == "__main__":
    a = [4,5,7,8,9,4,3,2,5,6,1]
    binary_search(a,9)