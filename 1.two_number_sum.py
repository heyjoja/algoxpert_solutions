def twoNumberSum(array, targetSum):
    target = []
    found = False
    for x in range(len(array)):
        for k in range(len(array)):
            if found: break
            if(x == k): 
                continue
            else:
                target = [array[x], array[k]] if array[x] + array[k] == targetSum else []
                found = True if array[x] + array[k] == targetSum else False
    return target
       
