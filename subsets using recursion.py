#method 1
import itertools

def generate_subsets_itertools(a):
    subsets = []
    for i in range(len(a) + 1):
        subsets.extend(itertools.combinations(a, i))
    return subsets

a = [1, 2, 3, 4, 5]
subsets = generate_subsets_itertools(a)
for subset in subsets:
    print(list(subset))


#**method 2

def printAllSubsets(nums, index, result, value):
    if index == len(nums):
        print(result)
        value[0] += 1
        return
 
    # Include 
    result.append(nums[index])
    printAllSubsets(nums, index + 1, result, value)
    result.pop()
 
    # Exclude
    printAllSubsets(nums, index + 1, result, value)
 
 
nums = [10, 20, 30, 40, 50, 60, 65]
 
value = [0]
printAllSubsets(nums, 0, [], value)
print(value[0])