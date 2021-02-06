
// https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3628/

package main

import (
	"fmt"
	"sort"
)

func main() {

	nums, err := intScanln(8)
	if err != nil {
		fmt.Println(err)
		return
	}

	sort.Ints(nums)

	fmt.Printf("%v\n", nums)

	// logic begins here

	start, end := 0, 1
	size := 0

	for end != len(nums) && start < end {
		diff := nums[end] - nums[start]

		if diff == 0 {
			end++
		} else if diff == 1 {
			end++
			diffBwEndStart := end - start
			if diffBwEndStart > size {
				size = diffBwEndStart
			}
		} else { // diff > 1

			if end - start == 1 {
				end++
			}

			start++
		}
	}

	println(size)
}

func intScanln(n int) ([]int, error) {
	x := make([]int, n)
	y := make([]interface{}, len(x))
	for i := range x {
		y[i] = &x[i]
	}
	n, err := fmt.Scan(y...)
	x = x[:n]
	return x, err
}
