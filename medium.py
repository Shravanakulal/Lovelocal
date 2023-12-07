def majority_elements(nums):
    if not nums:
        return []

    element1,count1 = None, 0
    element2,count2 = None, 0

    for num in nums:

        if element1 == num:
            count1 += 1
        elif element2 == num:
            count2 += 1

        elif count1 == 0:
            element1, count1 = num, 1

        elif count2 == 0:
            element2, count2 = num, 1

        else:
            count1 -= 1
            count2 -= 1


    count1 = count2 = 0
    for num in nums:
        if num == element1:
            count1 += 1

        elif num == element2:
            count2 += 1

    result = []
    n = len(nums)


    if count1 > n//3:
        result.append(element1)
    if count2 > n//3:
        result.append(element2)

    return result



nums = [3, 2]
output = majority_elements(nums)
print(output)
