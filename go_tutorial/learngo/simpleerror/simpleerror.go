package simpleerror

// Simple error
func New(text string) error {
	return &simpleError{text}
}

type simpleError struct {
	s string
}

func (e *simpleError) Error() string {
	return e.s
}
