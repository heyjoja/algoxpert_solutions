def twoNumberSum(array, targetSum):
    target = []
    for x in range(len(array)):
        if target != []: break
        target = [ [x,y] for y in range(len(array)) if( x != y) and (array[x] + array[y] == targetSum) ]
    return [ array[target[0][0]], array[target[0][1]] ] if len(target) > 0 else []
