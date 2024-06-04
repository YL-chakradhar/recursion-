#method1 

def printsum(index,n,nums,result,max1,min1):
    if index==n:
        print(result)
        print(max1)
        print(min1)
        return
    result+=nums[index]
    if max1<nums[index]:
        max1=nums[index]
    if min1>nums[index]:
        min1=nums[index]
    printsum(index+1,n,nums,result,max1,min1)
index=0
nums=[1,2,3,4,5]
n=len(nums)
max1=nums[index]
min1=nums[index]
print(printsum(0,n,nums,0,max1,min1))

#method2 


def printSum2(index, n, nums):
    if index == n:
        return 0 
    nextElementsSum = printSum2(index + 1, n, nums)
    return nextElementsSum + nums[index]
 
nums = [12, 34, 12, 5, 7]
n = len(nums)
print(printSum2(0, n, nums))

#max element
def max1(index, n, nums):
    if index == n - 1:
        return nums[index]
    nextMax = max1(index + 1, n, nums)
    if nums[index] > nextMax:
        return nums[index]
    else:
        return nextMax

nums = [12, 34, 12, 5, 7]
n = len(nums)
print(max1(0, n, nums))
