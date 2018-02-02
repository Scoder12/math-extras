def mode(nums):
    output = {}
    lsnum = None
    lock = 0
    amount = 0
    for x in range(len(nums)):
        if lock == 0:
            lock = 1
            lsnum = nums[x]
        if nums[x] != lsnum:
            output[lsnum] = amount
            lsnum = nums[x]
            amount = 0
            continue
        else:
            amount += 1
            continue
    return output
