package simpleinterest

import (
	"fmt"
	"log"
)

// you normally cannot import packages you don't use, but if you need to for development, you can use _ to bypass this
var _ = log.Fatal // this is called an error silencer, and should be at the top of the package.

// Notice the file name matches the name of the package. This is standard.

func init() { // We can initialize a package with init() there can be no params or return types. It runs after other imported packages are initialized and package level variables.
	fmt.Println("Simple interest package initialized")
}

// Calculate calculates and returns the simple interest for a principal p, rate of interest r for time duration t years
func Calculate(p float64, r float64, t float64) float64 { //We capitalize Calculate because we want it public - accessible outside the package.
	interest := p * (r / 100) * t
	return interest
}
