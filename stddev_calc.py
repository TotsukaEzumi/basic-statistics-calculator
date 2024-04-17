import math
import os
def bubble(arr):
    n = len(arr)
    for i in range (0,n-1):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr
    
def mean(arr):
    sum = 0
    for i in range (0, len(arr)):
        sum = sum + arr[i]
    return (sum/len(arr))

def median(arr):
    n = len(arr)
    if n%2 != 0:
        return arr[((n+1)//2)-1]
    elif n%2 == 0:
        pos1 = ((n+1)//2)-1
        pos2 = pos1+1
        newarr = [arr[pos1],arr[pos2]]
        return mean(newarr)
    
def stddev(arr, mean):
    partial_sum = 0
    n = len(arr)
    for i in range(0,n):
        value = (arr[i] - mean)*(arr[i] - mean)
        partial_sum = partial_sum + value
    sum = partial_sum/n
    return math.sqrt(sum)

def lowerQuartile(arr, med):
    newarr = []
    flag = False
    count = 0
    arr = bubble(arr)
    while flag == False:
        if arr[count] == med:
            break
        elif ((arr[count] < med)and(arr[count+1] > med)):
            newarr.append(arr[count])
            break
        else:
            newarr.append(arr[count])
            count = count +1
    return median(newarr)

def upperQuartile(arr, med):
    newarr = []
    flag = False
    count = len(arr)-1
    arr = bubble(arr)
    while flag == False:
        if arr[count] == med:
            break
        elif ((arr[count] > med)and(arr[count-1] < med)):
            newarr.append(arr[count])
            break
        else:
            newarr.append(arr[count])
            count = count -1
    return median(newarr)

def interquartileRange(a,b):
    return a-b

print("*******************************")
print("*******************************")
print("**** welcome to statistics ****")
print("************ mode *************")
print("*******************************")
print("*******************************")
print("please enter data values and please enter 'x' to see results")
print(os.getcwd())

arr = []

flag = False
while flag == False:
    data = input("Enter data: ")
    if data == "x":
        break
    else:
        arr.append(float(data))
        print(arr)
choice = int(input("\nnumber of columns : "))
if choice == 1:
    print("")
    print(f"Sorted array        : {bubble(arr)}\n")
    print(f"Mean                : {mean(arr)}")
    print(f"Median              : {median(arr)}")
    print(f"Standard Deviation  : {stddev(arr, mean(arr))}")
    print(f"Variance            : {(stddev(arr, mean(arr)))*(stddev(arr, mean(arr)))}")
    print(f"Minimum value       : {min(arr)}")
    print(f"Maximum value       : {max(arr)}")
    print(f"Lower quartile      : {lowerQuartile(arr, median(arr))}")
    print(f"Upper quartile      : {upperQuartile(arr, median(arr))}")
    print(f"Interquartile range : {interquartileRange(upperQuartile(arr, median(arr)), lowerQuartile(arr, median(arr)))}")
else:
    arr1 = []

    flag = False
    while flag == False:
        data = input("Enter column 2 : ")
        if data == "x":
            break
        else:
            arr.append(float(data))
            print(arr1)
    for i in range(0, len(arr1)):
        arr[i] = (arr1[i]*arr[i])
    print("")
    print(f"Sorted array        : {bubble(arr)}\n")
    print(f"Mean                : {mean(arr)}")
    print(f"Median              : {median(arr)}")
    print(f"Standard Deviation  : {stddev(arr, mean(arr))}")
    print(f"Variance            : {(stddev(arr, mean(arr)))*(stddev(arr, mean(arr)))}")
    print(f"Minimum value       : {min(arr)}")
    print(f"Maximum value       : {max(arr)}")
    print(f"Lower quartile      : {lowerQuartile(arr, median(arr))}")
    print(f"Upper quartile      : {upperQuartile(arr, median(arr))}")
    print(f"Interquartile range : {interquartileRange(upperQuartile(arr, median(arr)), lowerQuartile(arr, median(arr)))}")
    