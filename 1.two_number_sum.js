function twoNumberSum(array, targetSum) {
  let calculating = []
  let found = false
  for(let k = 0; k <= array.length; k++){
     for(let nk = 0; nk < array.length; nk++){
       if (found) break
       if(nk === k) continue
       calculating = (array[k] + array[nk] === targetSum) ? [array[k], array[nk]] : []
       found = (array[k] + array[nk] === targetSum)
     }
  }
  return calculating
}

// Do not edit the line below.
exports.twoNumberSum = twoNumberSum;
