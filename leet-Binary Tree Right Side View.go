// https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3630/

package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {

}

func rightSideView(root *TreeNode) []int {

	var rightSideViewList []int

	mapLevelElements := make(map[int][]int)
	//mapLevelElements[0] = append(mapLevelElements[0], root.Val)

	rightSideView2(root, mapLevelElements, 0)

	maplen := len(mapLevelElements)

	for i := 0; i < maplen; i++ {

		//var rightMostElement int
		//
		//for j := range mapLevelElements[i] {
		//	rightMostElement = mapLevelElements[i][j]
		//}

		rightSideViewList = append(rightSideViewList, mapLevelElements[i][0])
	}

	return rightSideViewList
}

func rightSideView2(root *TreeNode, mapLevelElements map[int][]int, level int) {
	if root == nil {
		return
	}

	mapLevelElements[level] = append(mapLevelElements[level], root.Val)

	rightSideView2(root.Right, mapLevelElements, level+1)
	rightSideView2(root.Left, mapLevelElements, level+1)
}
