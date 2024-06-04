nums = [-2,1,-3,4,-1,2,1,-5,4]
curr=0
max_sum=float('-inf')
for i in nums:
    curr+=i
    
    if curr<0:
        curr=0
    if max_sum<curr:
        max_sum=curr
print(max_sum)
#output is 
#The subarray [4,-1,2,1] has the largest sum 6.