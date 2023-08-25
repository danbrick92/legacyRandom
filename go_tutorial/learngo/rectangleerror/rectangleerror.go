package rectangleerror

// Rectangle Custom Error
type RectangleError struct {
	Err   string
	Side1 float64
	Side2 float64
}

func (e *RectangleError) Error() string {
	return e.Err
}

// Custom boolean functions to check what is wrong
func (e *RectangleError) Side1Negative() bool {
	return e.Side1 < 0
}

func (e *RectangleError) Side2Negative() bool {
	return e.Side2 < 0
}
