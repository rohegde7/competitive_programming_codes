// https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3629/

package main

import (
	"fmt"
	"strings"
)

func main() {
	var inputPath string
	var inputArr []string
	var output = ""

	var stack Stack // create a stack variable of type Stack

	//var outputPath *string = ""

	fmt.Scanln(&inputPath)
	inputArr = strings.Split(inputPath, "/")

	//if inputArr[1] != ".." {
	//stack.Push("/")
	//}

	//for i := range inputArr {
	//	println(inputArr[i])
	//}

	// logic begins...

	for i := range inputArr {

		ele := inputArr[i]

		switch ele {

		case ".":
			break

		case "..":

				stack.Pop()

			break

		case " ":
		case "":
			//if i != 0 {
			//	if inputArr[i-1] == "" || inputArr[i-1] == " " {
			//		stack.Push("/")
			//	}
			//}
			break

		default:
			stack.Push("/" + ele)
		}
	}

	for i := range stack {
		output += stack[i]
	}

	if output == "" {
		output = "/"
	}
	println(output)
}

type Stack []string

// IsEmpty: check if stack is empty
func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}

// Push a new value onto the stack
func (s *Stack) Push(str string) {
	*s = append(*s, str) // Simply append the new value to the end of the stack
}

// Remove and return top element of stack. Return false if stack is empty.
func (s *Stack) Pop() (string, bool) {
	if s.IsEmpty() {
		return "", false
	} else {
		index := len(*s) - 1   // Get the index of the top most element.
		element := (*s)[index] // Index into the slice and obtain the element.
		*s = (*s)[:index]      // Remove it from the stack by slicing it off.
		return element, true
	}
}
