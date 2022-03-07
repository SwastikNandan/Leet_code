def checkSubarraySum(nums, k):
    remainder = { 0: -1} #mapping remainder to ending index of the sub array
    total = 0

    for i,n in enumerate(nums):
        total += n
        r = total % k
        if r not in remainder:
            remainder[r] = i
        elif i - remainder[r] > 1:
            return True
    return False