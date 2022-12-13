package main

func TwoNumberSum(array []int, target int) []int {
	// Write your code here.
    var targetValues = make([]int, 0)
    var found bool
    for k, v := range(array){
        for x1, v1 := range(array){
            if found {
                break
            }

            if k != x1 {
                if v + v1 == target {
                    targetValues = append(targetValues, array[k], array[x1])
                    found = true
                }
            }
        }
    }
    return targetValues
}
