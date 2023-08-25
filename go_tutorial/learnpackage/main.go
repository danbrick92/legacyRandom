package main

import (
	"fmt"
	"learnpackage/simpleinterest" // we import the simpleinterest package.
)

func main() {
	fmt.Println("Simple interest calculation")
	p := 5000.0
	r := 10.0
	t := 1.0
	si := simpleinterest.Calculate(p, r, t) // note how we are referring to the package
	fmt.Println("Simple interest is", si)
}

/*
How does go install work?
It looks in the current directory for go.mod. When we open that, you can see it calls out a module learnpackage.
If there is no mod file, it won't find the module.
*/
