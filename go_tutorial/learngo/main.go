package main

import (
	"errors"
	"fmt"
	"learngo/armor"
	"learngo/income"
	"learngo/rectangleerror"
	"learngo/salarycalc"
	"learngo/simpleerror"
	"learngo/weapon"
	"net"
	"os"
	"path/filepath"
	"sync"
	"time"
)

func printHelloWorld() {
	fmt.Println("Hello world!")
}

func printAge() {
	var age int // gets initialized to 0 automatically
	fmt.Println("Their age is", age)
	age = 31 // you can update the variable as you go
	fmt.Println("My age is", age)
	var age2 int = 29 // you can also intialize the variable when you define it
	fmt.Println("Her age is", age2)
	var age3 = 46 // go can also infer the type
	fmt.Println("His age is", age3)
}

func printWidthHeight() {
	var height, width = 10, 20 // you can also declare multiple variables in one line
	fmt.Println("The height is ", height, " The width is ", width)
}

func printPersonInfo() {
	var (
		name = "Dan"
		age  = 31
	) // you can define variables of different types in one statement like this
	fmt.Println("His name is ", name, " and his age is ", age)
}

func shorthandDeclaration() {
	age := 31 // instead of sasying var age = 31, you can do shorthand and say age := 31, which declares and initializes it
	fmt.Println("His age is ", age)
	name, age1 := "dan", 31 // you can define multiple variables of different types on one line with shorthand
	fmt.Println("His name is ", name, " and his age is ", age1)
	name, age2 := "cheryl", 29 // note that you only use := when at least 1 of the variables is new
	fmt.Println("Her name is ", name, " and his age is ", age2)
}

func types() {
	// bool: true or false
	// ints: int8 - int64, int is either 32 or 64 depending on platform
	// uints: unint8 - unint64
	// floats: 32 or 64
	// complexes: 64 or 128. Supports real and imaginary numbers.
	// byte: alias of uint8
	// rune: alias of int32
	// string
}

func typeConversions() {
	// Go very strict about typing
	i := 55
	j := 67.8
	sum := i + int(j)
	fmt.Println(sum)
	// casting to float
	i = 10
	var a float64 = float64(i)
	fmt.Println(a)
	// there are a lot of other typecasts available
}

func constants() {
	const a = 50
	fmt.Println(a)
	const (
		b = 51
		c = 52
	)
	fmt.Println(b, c)
	// you may not reassign a value to a constant
	// the value must be known at compile time
	// (ie: you cannot say const b = Math.sqrt(4))
	const dan = "dan" // string constants are considered untyped ...
	// unless a line of code demands it!
	const bill string = "bill" // you could also declare it explicity
	// booleans have the same rules as string constants do - untyped unless otherwise
}

func testDivision() {
	a := 5.9 / 8 // automatically becomes a float
	fmt.Println(a)
}

func funcWithParameters(price int, no int) int {
	// this function takes two integers, multiplies them, and returns an int
	totalPrice := price * no
	return totalPrice
}

func funcWithParameters2(price, no int) int {
	// this function takes two integers, multiplies them, and returns an int
	// note how we can remove redundant typing
	totalPrice := price * no
	return totalPrice
}

func funcWithMultipleReturns(length, width float64) (float64, float64) {
	// You can return multiple parameters with Go
	area := length * width
	perimeter := (length + width) * 2
	return area, perimeter
}

func returnNamedParameters(length, width float64) (area, perimeter float64) {
	// We can also choose to automatically return the values specified in return clause
	area = length * width
	perimeter = (length + width) * 2
	return
}

func conditionals(height, width int) {
	/*
		else if and else have to be on the same line as } terminator
		go interprets a line break as a ; thus it thinks the conditional is over)
	*/

	if height*width >= 100 {
		fmt.Println("Big")
	} else if (height*width < 100) && (height*width >= 50) {
		fmt.Println("Medium")
	} else {
		fmt.Println("Small")
	}
}

func assignment_if(value int) {
	if value = value + 1; value%2 == 0 { // kind of wierd but you can perform an assignment before checking the conditional
		fmt.Println("Even")
	} else {
		fmt.Println("Odd")
	}
}

func idiomatic_if(value int) {
	// the correct way to write go is to avoid as much indentation as possible and return early
	if value%2 == 0 {
		fmt.Println(value, "is even")
		return
	}
	fmt.Println(value, "is odd")
}

func loop_basic() {
	// there are only for loops in go.
	for i := 0; i < 10; i++ { //classic for loop syntax
		if i%2 == 0 {
			continue // continue and break statements as usual
		} else if i == 9 {
			break
		}
		fmt.Println(i)
	}
}

func crazy_loop() {
	for no, i := 10, 1; i <= 10 && no <= 19; i, no = i+1, no+1 { //multiple initialisation and increment
		fmt.Printf("%d * %d = %d\n", no, i, no*i)
	}
}

func nested_labeled_loop() {
	// You can label your loops and then choose which loop you want to break
outer:
	for i := 0; i < 3; i++ {
	inner:
		for j := 1; j < 3; j++ {
			for k := -1; k < 1; k++ {
				if j == i {
					break outer
				}
				if k == j {
					break inner
				}
				fmt.Println(i, j, k)
			}
		}
	}
}

func infiniteLoop() {
	for { // this is an infinite loop - don't run it

	}
}

func printFinger(fingerNum int) {
	// Switch/case syntax, does not have to include break though
	fmt.Printf("Finger %d is ", fingerNum)
	switch fingerNum {
	case 1:
		fmt.Println("Thumb")
	case 2:
		fmt.Println("Index")
	case 3:
		fmt.Println("Middle")
	case 4:
		fmt.Println("Ring")
	case 5:
		fmt.Println("Pinky")
	default:
		fmt.Println("Failure")
	}
}

func checkIsVowel(letter string) bool {
	switch letter {
	case "a", "e", "i", "o", "u": // note that you can use multiple values in a single case
		return true
	}
	return false
}

func checkTruth(value int) {
	switch { // you can omit the expression to be evaluated here, letting you use typical if condition operators
	case value < 0: // by default will use the first case that applies, (-2 here would meet both criteria, but only print Negative.)
		fmt.Println("Negative")
	case value%2 == 0:
		fmt.Println("Even")
		fallthrough // using fallthrough here will also run the statements in the very next case statement (even if the condition is not met)
	case value%2 != 0:
		fmt.Println("Odd")
		break // you can use break to exit the switch
	}
}

func arrays() {
	// init and then declare
	var arr [3]int // auto initializes all elements to 0
	arr[0] = 1
	arr[1] = 2
	arr[2] = 3

	a := [3]int{1, 2, 3} // short-hand declaration
	fmt.Println(a)       // you can print out arrays

	// you don't have to assign a value to each item short-hand
	b := [3]int{12}
	fmt.Println(b)

	// what do strings auto-init to? blank strings
	var arr2 [3]string
	fmt.Println(arr2)
	fmt.Println(arr2[0] == "") // prints true

	// the size of the array is part of the type - can't assign a 3 element array to one with 5 elements
	// arrays are values and not references - so if you assign the array to a new variable, a copy is assigned.
	x := [...]int{1, 2} // note the usage of ..., this lets the compiler interpret the correct size
	y := x
	y[0] = 0 // only modifies y and not x
	fmt.Println(x, y)

	// arrays are also passed by value to functions as parameters
	fmt.Println(len(arr)) // getting the length of an array

	// iterating over an array (there are better ways than the traditional for loop)
	for i, v := range arr { // we get both the index and value of the array by using range in this way
		fmt.Printf("%d the element of a is %v\n", i, v)
	}

	// multidimensional arrays
	phones := [2][2]string{
		{"galaxy", "note"},
		{"iphone", "ipod"},
	}
	fmt.Println(phones)
}

func editNumbers(numbers []int) {
	for i := range numbers {
		numbers[i]++
	}
}

func slices() {
	// This allows you to create slices from the array
	a := [5]int{76, 77, 78, 79, 80}
	var b []int = a[1:4] // the first number is inclusive, the last is exclusive, so we get indexes 1, 2, 3
	fmt.Println(b)

	// Creating an array from a slice
	c := []int{1, 2, 3}
	fmt.Println(c)

	// Modifying a slice does modify the underlying array
	darr := [...]int{57, 89, 90, 82, 100, 78, 67, 69, 59}
	dslice := darr[2:5]
	fmt.Println("array before", darr)
	for i := range dslice {
		dslice[i]++
	}
	fmt.Println("array after", darr)

	// this also means that if we have two slices that overlap in the same array, changes will show on both slices

	// length and capacity of a slice ...
	// the length of the slice is the number of elements in the slice
	fruitarray := [...]string{"apple", "orange", "grape", "mango", "water melon", "pine apple", "chikoo"}
	fslice := fruitarray[1:3]
	fmt.Println(len(fslice)) // the length is 2

	// the capacity of the slice is the number of elements in the underlying array
	// starting from the index from which the slice is created.
	fmt.Println(cap(fslice)) // the capacity is 6 (orange, grape, "", "", "", "")

	// Can I make a slice from scratch?
	i := make([]int, 5, 5) // make does this, it creates an underlying [] with 5 elements, and then sets a len and cap of 5
	fmt.Println(i)

	// Can I append to a slice?
	i = append(i, 1, 2, 3) // yes
	fmt.Println(i)
	// What happened to length and capacity?
	fmt.Println(len(i), cap(i)) // len is 8, cap is 10. The capacity doubles when we spill over.

	// What about nil slices
	var names []string
	if names == nil {
		fmt.Println("slice is nil going to append")
		names = append(names, "John", "Sebastian", "Vinay")
		fmt.Println("names contents:", names)
	}

	// You can append two slices to eachother
	fruits := []string{"apples", "oranges", "bananas"}
	veggies := []string{"brocolli", "peas", "beans"}
	produce := append(fruits, veggies...)
	fmt.Println("produce contents:", produce)

	// Because slices rely on pointers, they do edit the underlying array even if passed to a function
	// That is because slices data structures are just the len, cap, and a pointer to the first list item
	// When it copies the slice to the function, it's just a copy of the pointer, not what the pointer refers to
	fmt.Println("array before", i)
	editNumbers(i)
	fmt.Println("array after", i)

	// You can do multi-dimensional slices
	multidimSlice := [][]string{
		{"PC", "Windows"},
		{"Mac"},
	}
	fmt.Println(multidimSlice)

	// As long as a slice is in memory, the underlying array cannot be garbage collected
	// So if you are operating under a subslice and don't need the underlying array, you should use copy
	countries := []string{"USA", "Singapore", "Germany", "India", "Australia"}
	neededCountries := countries[:len(countries)-2]
	countriesCpy := make([]string, len(neededCountries))
	copy(countriesCpy, neededCountries) // if we return countriesCpy, neededCountries will be garbage collected then
}

func variadicNumFunction(num int, nums ...int) int { // the variable param must come last
	// variadic means it takes a variable number of params
	// under the hood, it creates a slice of the variadic param
	for i := range nums {
		if nums[i] == num {
			fmt.Println("Index of 10 ", i)
			return i
		}
	}
	return -1
}

func maps() {
	// you can initiate a map like this:
	employeeSalary := make(map[string]int)
	employeeSalary["dan"] = 155000
	employeeSalary["carly"] = 80000
	fmt.Println(employeeSalary)

	// or like this:
	nameAge := map[string]int{
		"dan":   30,
		"carly": 4,
	}
	fmt.Println(nameAge)

	// you have to initialize the map before trying to add contents to it

	// you can access contents of the map easily
	myAge := nameAge["dan"]
	fmt.Println(myAge)

	// what if the key isn't present?
	newAge := nameAge["fakeName"]
	fmt.Println(newAge) // its set to 0

	// how to check if value is present
	_, ok := nameAge["fakeName"] // the second variable tells us if the key was found
	fmt.Println(ok)

	// iterate over all elements in map
	for key, value := range nameAge {
		fmt.Printf("nameAge[%s] = %d\n", key, value)
	}

	// delete item from map
	delete(nameAge, "dan")

	// you can also use objects as values in the map
	// you can use len() to get number of keys in map

	// maps are reference types, so passing the map name will just pass a reference to it
	employeeSalary2 := map[string]int{
		"steve": 12000,
		"jamie": 15000,
		"mike":  9000,
	}
	fmt.Println("Original employee salary", employeeSalary2)
	modified := employeeSalary2
	modified["mike"] = 18000
	fmt.Println("Employee salary changed", employeeSalary2)
}

func mutate(s []rune) string {
	s[0] = 'a'
	return string(s)
}

func strings() {
	// a string is a slice of bytes
	name := "Hello World"
	fmt.Printf("String: %s\n", name)

	// since it is a string of bytes, you can acces each byte
	fmt.Printf("%x ", name[0])

	// accessing each charcter can be done via [] notation
	fmt.Printf("%c ", name[0])

	// checking if two strings are equal is easy
	fmt.Println(name == "Dan")

	// concatenating strings is easy
	a := "Hello " + "World"
	fmt.Println(a)

	// strings are considered immutable in Go, thus you cannot modify them in place
	// to get around this you have to convert them to a slice of runes anf then it's converted back to a string
	fmt.Println(mutate([]rune(a)))
}

func returnPointer() *int {
	a := 10
	b := &a
	return b
}

func passPointer(point *int) {
	fmt.Println("Received pointer with value ", point)
}

func pointers() {
	// pointers are declared with *type
	b := 255
	var a *int = &b // & gets the address of a variable
	fmt.Printf("Type of a is %T\n", a)
	fmt.Println("address of b is", a)

	// a pointer that has not been initialized will have a value of nil

	// We can return pointers back from functions
	retval := returnPointer()
	fmt.Println(retval)

	// You can deference the pointer to get the value
	fmt.Println(*retval)

	// You can create a pointer to specific type with the new keyword
	c := new(int)
	fmt.Printf("Size value is %d, type is %T, address is %v\n", *c, c, c)

	// You can pass pointers to other functions
	passPointer(c)

	// Do not pass pointers to arrays to other functions - use slices (it works, but its not idiomatic)
	// Go does not support pointer arithmetic
}

type person struct {
	name string
	age  int
	data map[string]int
}

type testy struct {
	name string
	age  int
}

type employee struct { // you can define attributes of same type on one line
	fname, lname string
	id           int
}

func structs() {
	// can compare structs made up of primitives
	a := testy{
		name: "test",
		age:  30,
	}

	b := testy{
		name: "test",
		age:  30,
	}

	fmt.Println(a == b)

	// cannot compare structs that have uncomparable data types
	danData := make(map[string]int)
	danData["test"] = 123
	dan := person{
		name: "Dan",
		age:  30,
		data: danData,
	}

	cheryl := person{
		name: "Cheryl",
		age:  29,
		data: danData,
	}
	fmt.Println(dan, cheryl)

	// Anonymous structs - one time use structs
	emp3 := struct {
		firstName string
		lastName  string
		age       int
		salary    int
	}{
		firstName: "Andreah",
		lastName:  "Nikola",
		age:       31,
		salary:    5000,
	}
	fmt.Println(emp3)

	// You use . syntax to access a variable of the struct
	fmt.Println(emp3.age)

	// What happens if we do not init the struct - it uses default 0 or "" values
	var carly person
	fmt.Println(carly.name) // will be blank string

	// You can also specify some values for fields and ignore the rest
	// You can create pointers to structs
	cherylPtr := &cheryl
	fmt.Println(*cherylPtr)

	// Anonymous fields - we can not include name fields and access them using their data type (but cannot reuse datatype)
	type Dog struct {
		string
		int
	}
	max := Dog{"boxer", 10}
	fmt.Println(max.string)

	// Nested structs
	type Address struct {
		streetnum int
		roadname  string
	}
	type House struct {
		address Address
		color   string
	}
	myhouse := House{
		address: Address{150, "Scotland Drive"},
		color:   "grey",
	}
	fmt.Println(myhouse)

	// Promoted fields - if you make the inner struct anonmyous, the fields inside that get promoted to the outside
	type House2 struct {
		Address
		color string
	}
	myhouse2 := House2{
		Address{150, "Scotland Drive"},
		"grey",
	}
	fmt.Println(myhouse2.streetnum)

	// If you capitalize the name of a struct, then it is exported and can be accessed from other packages
	// Like maps, structs are considered equal if their contents are equal
	// They cannot be compared if they have fields that are not comparable
}

func (e employee) displayId() { // Note how there are two () -> the first is the struct, the second are params
	fmt.Println(e.id)
}

func (e employee) editId() {
	e.id = 10
}

func (e *employee) editIdByRef() {
	e.id = 10
}

// Workaround for defining method on predefined type
type myInt int

func (i myInt) printMyInt() {
	fmt.Println(i)
}

func methods() {
	// Methods are functions with special Type receivers at the beginning
	dan := employee{
		fname: "dan",
		lname: "brickner",
		id:    17,
	}
	dan.displayId()

	// Methods are used for operations on structs to replace OOP in other languages
	// Methods can also have the same names on different types

	// Methods still pass the struct by value, so it's copied
	dan.editId()
	fmt.Println(dan.id) // notice how the id didn't change

	// If you want to edit the original object, pass a pointer to it instead
	d := &dan
	d.editIdByRef()
	fmt.Println(dan.id) // notice how the id didn't change

	// Methods that belong to an anonymous field of a struct can be called as
	// if they belong to the structure where the anonymous field is defined

	// When a function has a value receiver (ie: int), you can only pass by value (ie: dan = struct; dan.area())
	// When a method has a value receiver, you can pass both by value and by pointer (ie: dan = struct; d = &dan; d.area())
	dan.displayId()
	d.displayId()

	// Methods with pointers for receivers also accept values
	dan.editIdByRef() // see how we used dan the value but called a method using a ptr

	// You can actually create methods on non-struct types
	// The trick is that to define a method on a type, the definition of the type and methods must be in the
	// same package.
	num1 := myInt(18)
	num1.printMyInt()
}

// Interface definitions - see interfaces() for more on this below
type VowelsFinder interface {
	FindVowels() []rune
}
type MyString string

func (ms MyString) FindVowels() []rune {
	var vowels []rune
	for _, rune := range ms {
		if rune == 'a' || rune == 'e' || rune == 'i' || rune == 'o' || rune == 'u' {
			vowels = append(vowels, rune)
		}
	}
	return vowels
}

// More interface definitions
type Worker interface {
	Work()
}

type Person struct {
	name string
}

func (p Person) Work() {
	fmt.Println("\n", p.name, " is working\n")
}

func describe(w Worker) {
	fmt.Printf("Interface type %T value %v\n", w, w)
}

// Empty interface method - any type can be passed in!
func describe1(i interface{}) {
	fmt.Printf("Type = %T, value = %v\n", i, i)
}

func assert(i interface{}) {
	s := i.(int) //get the underlying int value from i
	fmt.Println(s)
}

func assert2(i interface{}) {
	v, ok := i.(int) //get the underlying int value from i
	fmt.Println(v, ok)
}

func findType(i interface{}) {
	switch i.(type) {
	case string:
		fmt.Printf("I am a string and my value is %s\n", i.(string))
	case int:
		fmt.Printf("I am an int and my value is %d\n", i.(int))
	default:
		fmt.Printf("Unknown type\n")
	}
}

func checkInterface(i interface{}) {
	switch v := i.(type) {
	case Worker:
		fmt.Printf("Implements interface\n")
		v.Work()
	default:
		fmt.Printf("Does not implement interface\n")
	}
}

func interfaces() {
	// An interface is a set of method signatures
	// When a type provides definitions for all the methods in an interface, it is said to implement that interface
	// The interface specifies what methods a type should have
	// A type decides exactly how to implement that
	// IE: WashingMachine might have an interface with methods Wash() and Dry()
	// Any type that has both these methods is implementing that interface

	// Notice above how MyString implements all methods needed for interface VowelsFinder.
	// This means we can more generically call the interface and trust the underlying method for the implementation
	name := MyString("Dan Brickner")
	var v VowelsFinder
	v = name
	fmt.Printf("Vowels are %c", v.FindVowels())

	// Notice how we do not explicitly say we implement the interface - it just happens if we implement all the methods

	// Going to create a separate module where I get more into interfaces. This is using an exported example
	dan := salarycalc.Employee{
		Name:        "dan",
		Salary:      50000,
		Performance: 40000,
	}
	employees := []salarycalc.SalaryCalculator{dan}
	x := salarycalc.TotalExpense(employees)
	println(x)

	// Empty interfaces - an interface that has 0 methods - thus all types implement this interface
	describe1(5)
	describe1("test")
	describe1(dan)

	// Interfaces are represented in memory as a tuple of (type, value)
	// The interface is itself the type, and the value would be the concrete implementation of that interface
	cheryl := Person{
		name: "cheryl",
	}
	var v1 Worker
	v1 = cheryl
	v1.Work() // the concrete type of v1 is Person
	describe(v1)

	// Extracting the underlying value of an interface - type assertion
	// We use i.(Type) in the function to extract the underlying value of the interface
	var integerGuy interface{} = 56
	assert(integerGuy)

	// What if it's not an int?
	var stringGuy interface{} = "guy" // creates a panic, an error
	// assert(stringGuy)

	// To solve this issue, we can use the following syntax: v, ok := i.(T)
	// If the type is wrong, we get the 0 value type fo v and ok is set to false
	assert2(stringGuy) // prints 0, false

	// Type switch - you can compare the types of an interface using a switch i.(Type)
	findType(stringGuy)
	findType(integerGuy)
	findType(dan)

	// Checking to see if a type implements an interface
	checkInterface(stringGuy)
	checkInterface(cheryl)
}

///////

type Describer interface {
	Describe()
}

type Smeller interface {
	Smell()
}

type Fooder interface {
	Describer
	Smeller
}

type Food struct {
	name  string
	taste string
	smell string
}

func (f *Food) Describe() {
	fmt.Println("Tastes", f.taste)
}

func (f *Food) Smell() {
	fmt.Println("Smells", f.smell)
}

func interfaces2() {
	// You can implement an interface using pointer receivers as well
	f := Food{
		name:  "watermelon",
		taste: "sweet",
		smell: "melon-like",
	}
	var f1 Describer = &f
	f1.Describe()

	// This will create problems - Food's describe method is designed to take a pointer not the value
	// Why? It is legal to call a pointer-value on anything that is already a pointer or whose address can be taken.
	// The concrete value stored in an interface is NOT addressable, thus the compilre cannot automatically get the address, and it fails
	// var f2 Describer
	// f2 = f
	// f2.Describe()

	// You can implement multiple interfaces
	// We already know Food implements the Describer interface, but it can do the same to Smeller
	var f3 Smeller = &f
	f3.Smell()

	// Embedding interface - creating interfaces out of other interfaces (Fooder uses both Smeller and Describer) - kind of like inheritance
	var f4 Fooder = &f
	f4.Describe()
	f4.Smell()

	// Zero value of an interface - nil
	var d1 Describer
	if d1 == nil {
		fmt.Printf("d1 is nil and has type %T value %v\n", d1, d1)
	}
	// d1.Describe() // this will panic - this is not concretely implemented
}

func concurrency() {
	/*
		Go supports concurrency, not parallelism

		Concurrency: (task1 = -; task 2 = x )
		----xxxx----xxxx----xxxx----

		Paralellism:
		----------
		xxxxxxxxxx
	*/
}

func numbers() {
	for i := 1; i < 10; i++ {
		fmt.Println(i)
		time.Sleep(100 * time.Millisecond) // using sleeps just for example
	}
}

func alphabet() {
	letters := []string{"a", "e", "i", "o", "u"}
	for _, v := range letters {
		fmt.Println(v)
		time.Sleep(200 * time.Millisecond) // using sleeps just for example
	}
}

func goroutines() {
	/*
		Go routines are like extremely lightweight threads

		- Sizing
			- They are only a few KB in size and can grow or shrink depending on the needs of an app
			- Traditional threads are are large and fixed size
		- Multiplexing
			- There could be a program that runs on 1 thread but has 1000 goroutines on it
			- If any routine blocks for user input, go will create a new os thread and move those routines to it
		- Channels
			- Goroutines communicate using channels - these are like pipes
			- By design, these prevent race conditions from happening when accessing shared memory
				- race condition = A race condition occurs when two or more threads can access shared data and they try to change it at the same time.
	*/
	go numbers()
	go alphabet()
	time.Sleep(3000 * time.Millisecond) // using sleeps just for example
}

func helloworldConcurrent(done chan bool) {
	fmt.Println("Hello World")
	done <- true // we signify the completion of the program with done
}

func calcArea(side1 float32, side2 float32, area chan float32) {
	prod := side1 * side2
	area <- prod
}

func calcPerimeter(side1 float32, side2 float32, perimeter chan float32) {
	per := (2.0 * side1) + (2.0 * side2)
	perimeter <- per
}

func writeSomeData(sendch chan<- int) { // we've made the chan unidirectional (send only) here
	data := 10
	sendch <- data
}

func channelCloser(heyChan chan int) {
	heyChan <- 10
	close(heyChan) // this'll close the channel
}

func channels() {
	// Like pipes. Just how water flows from one end of a pipe to another
	// data can be sent on one end and received on the other end with channels

	// You have to define the channels type - only this type can be sent through the channel
	// a := make(chan int)

	// You communicate to the channel by either sending or receiving data
	// data := <- a  // this is reading data from a channel
	// a <- data // this is writing data to a channel

	// Let's do a helloworld example
	done := make(chan bool) // done will signify when the program is complete running
	go helloworldConcurrent(done)
	<-done // This waits for done to send something back
	fmt.Println("All done now")

	// Let's do an example with two goroutines running at the same time
	areaCh := make(chan float32)
	perimeterCh := make(chan float32)
	var side1, side2 float32 = 30.4, 50.6
	go calcArea(side1, side2, areaCh)
	go calcPerimeter(side1, side2, perimeterCh)
	area, perimeter := <-areaCh, <-perimeterCh // this gets the correct values
	fmt.Println(area, perimeter)

	/*
		If a Goroutine is sending data on a channel, then it is expected that some other Goroutine
		should be receiving the data. If this does not happen, then the program will
		panic at runtime with Deadlock

		If a Goroutine is waiting to receive data from a channel,
		then some other Goroutine is expected to write data on that channel,
		else the program will panic.

	*/
	// The code below will panic because we wrote to a channel but no one received it
	// ch := make(chan int)
	// ch <- 5

	// Unidirectional channels - so far we have been only using bidirectional channels
	// In other words, data can be sent and received on them
	// You can create channels that can only send or only receive
	// The purpose behind this is that a bidirectional channel can be converted to one way
	// Comes in handy when we pass the chan into a function where we only want it to write
	// But the main program might need to do both
	// Example:
	bichan := make(chan int) // it is bidirectional here
	go writeSomeData(bichan)
	fmt.Println(<-bichan)

	// You can close channels and also check if they are still open
	heyChan := make(chan int)
	for {
		go channelCloser(heyChan)
		value, ok := <-heyChan // here we can use the extra ok option to see if the channel is still open
		if !ok {
			break
		}
		fmt.Println("Received ", value, ok)
	}

	// This can be done even more succinctly
	heyChan2 := make(chan int)
	go channelCloser(heyChan2)
	for v := range heyChan2 { // the range keeps checking ok until its not
		fmt.Println("Received ", v)
	}
}

func nameWriter(wCh chan string) {
	wCh <- "Dan"
	wCh <- "Birdie"
}

func basicChannelIterator(wCh chan int) {
	for i := 0; i < 10; i++ {
		wCh <- i
	}
	close(wCh)
}

func bufferedChannels() {
	/*
		So far we have been using unbuffered channels. As soon as data is sent, it blocks
		A buffered channel lets you specify a capacity before it blocks
	*/
	// Simple example
	wCh := make(chan string, 2) // The second argument here is the capacity
	go nameWriter(wCh)
	fmt.Println(<-wCh)
	fmt.Println(<-wCh)

	// A little more complicated
	wCh2 := make(chan int, 2)
	storedValues := make([]int, 0)
	go basicChannelIterator(wCh2)
	for v := range wCh2 {
		storedValues = append(storedValues, v)
	}
	fmt.Println(storedValues)

	/*
		This program will cause a deadlock. Since we are not reading off the channel concurrently,
		steve can never be written due to overcapacity, and we deadlock.
		ch := make(chan string, 2)
		ch <- "naveen"
		ch <- "paul"
		ch <- "steve"
		fmt.Println(<-ch)
		fmt.Println(<-ch)
	*/

	// You can continue to read off a closed channel if it still has values not yet read

	// Length - the length of the bufferedchannel is how many things are actually written in it
	// Capacity - the capactiy is the max size of the channel (we specify)
	ch := make(chan string, 3)
	ch <- "naveen"
	ch <- "paul"
	fmt.Println("capacity is", cap(ch))
	fmt.Println("length is", len(ch))
	fmt.Println("read value", <-ch)
	fmt.Println("new length is", len(ch))
}

func process(i int, wg *sync.WaitGroup) {
	fmt.Println("started Goroutine ", i)
	time.Sleep(2 * time.Second)
	fmt.Printf("Goroutine %d ended\n", i)
	wg.Done()
}

func workerPools() {
	/*
		WaitGroups - used to wait for a collection of goroutines to finish executing
		Lets say we have 3 goroutines running that need to finish before we can end our main function

		The weight group is basically a counter. When you call Add, it adds x to its counter
		When you call Done(), it decrements it by one
		Then the wait process basically waits until the counter is 0
	*/
	no := 3               // we will spawn off three processes
	var wg sync.WaitGroup // creation of the wait group
	for i := 0; i < no; i++ {
		wg.Add(1)          // now we add one item to the wait group
		go process(i, &wg) // and we pass the reference so at the completion of the routine it can signal done
		// Note above that we pass the pointer in (otherwise it will pass by value and get a copy, doesn't work)
	}
	wg.Wait() // now it waits for those processes
	fmt.Println("All go routines finished executing")

	/*
		Worker Pools - a collection of threads that are waiting for tasks to be assigned to them
		Once they finish the task assigned, they make themselves available again for the next task.

		This will be done in a seperate module called learnworkerpools

	*/

}

// ///
func server1(ch chan string) {
	time.Sleep(6 * time.Second)
	ch <- "from server1"
}

func server2(ch chan string) {
	time.Sleep(3 * time.Second)
	ch <- "from server2"
}

func selectStatement() {
	// The select statement is like a case-switch, but for selecting/receiving channels
	output1 := make(chan string)
	output2 := make(chan string)

	go server1(output1)
	go server2(output2)

	select { // the select statement blocks until one of the channels is ready and then terminates
	case s1 := <-output1:
		fmt.Println(s1)
	case s2 := <-output2:
		fmt.Println(s2) // in this case, we will print this due to the sleep
	}

	/*
		Purpose: As you can see, it only blocks until one channel is ready and ignores the rest.
		So why is that useful?

		Let's say we have an application that is super time-sensitive, and we send requests to 2 servers
		We take the response back from the first server that gets it and ignore the other.
	*/

	// Using the default case - used to prevent blocking
	// Below will print Still waiting 5 times before printing the response
	output3 := make(chan string)
	go server1(output3)
outer:
	for {
		time.Sleep(1 * time.Second)
		select {
		case s3 := <-output3:
			fmt.Println("Received response", s3)
			break outer
		default:
			fmt.Println("Still waiting on response")
		}
	}

	// Default cases can prevent deadlocks from occuring
	var chDead chan string
	select {
	case v := <-chDead: // this is deadlock, nothing will be sending data
		fmt.Println("received value", v)
	default:
		fmt.Println("default case executed")
	}

	// If multiple cases are ready at the same time, select will pick one at random
	// A blank select statement will cause a deadlock panic
}

var sharedInt = 0
var sharedInt2 = 0

func increment(wg *sync.WaitGroup, m *sync.Mutex) {
	m.Lock()
	sharedInt = sharedInt + 1
	m.Unlock()
	wg.Done()
}

func increment2(wg *sync.WaitGroup, ch chan bool) {
	ch <- true // if the channel is free, we aquired the lock. If not, then we have to wait until the channel has capacity.
	sharedInt2 = sharedInt2 + 1
	<-ch // this is the unlock, it reads from the channel and frees the capacity.
	wg.Done()
}

func mutexes() {
	/*
		Critical section - when a program runs concurrently, parts of code that modify
		shared resources should not be modified by multiple goroutines concurrently.
		This section of code is called the critical section.

		Let's say we have a variable x, we have a goroutine that increments it by 1
		Normally, this operation would get the value of x, compute x + 1, and assign that value to x.

		But if we have two goroutines simulatenously performing that operation, what happens?
		Ideally, the value should be x = 2.

		But the order of events could be:
			1) R1 gets the value of x = 0
			2) R2 gets the value of x = 0
			3) R1 computes x + 1 = 1
			4) R2 computes x + 1 = 1
			5) R1 assigns x = 1
			6) R2 assigns x = 1
		So x = 1, which is not right

		But in other cases it could be 2:
			1) R1 gets the value of x = 0
			2) R1 computes x + 1 = 1
			3) R1 assigns x = 1
			4) R2 gets the value of x = 1
			5) ... you can see how x will = 2

		This undesirable unpredictable situation is called a race condition
		Mutexes make it possible so that only one goroutine can access one critical section of code at a time.
	*/
	// Mutex Lock and Unlock make sure only one goroutine has access to that code at a time
	// If one goroutine has the lock, other must wait until it's unlocked.

	// Example
	noProcesses := 5      // we will spawn off five processes
	var wg sync.WaitGroup // creation of the wait group
	var m sync.Mutex      // creation of the Mutex
	for i := 0; i < noProcesses; i++ {
		wg.Add(1)
		go increment(&wg, &m) // note how we pass in the pointer to the mutex and waitgroup
	}
	wg.Wait()
	fmt.Println("The final incremented value is", sharedInt)

	// You can also solve race conditions using channels
	ch := make(chan bool, 1) // we create a buffered channel of 1 (unbuffered channels have a capacity of 0, meaning something must be there immediately to pick up the data)
	for i := 0; i < noProcesses; i++ {
		// because it only has a capacity of 1 and we write to the same channel,
		// it blocks other programs until the channel is free
		wg.Add(1)
		go increment2(&wg, ch)
	}
	wg.Wait()
	fmt.Println("The final incremented value is", sharedInt2)

	/*
		When to use mutexes vs. channels?
		Use channels when the goroutines need to communicate with one another.
		Use mutexes when only one goroutine should access the critical section of code.

		The above code is better solved using mutexes.

		Simply put, the mutex is the better choice to make sure only one goroutine is accessing the critical section of code.
	*/
}

func oop() {
	/*
		Go is not an object oriented language. But you use structs and methods instead of classes.
		In this example, we provide the "object" inside it's own package, which mimics how a class functions.
	*/
	// sword := weapon.Weapon{
	// 	Name:   "Fury",
	// 	Type:   "Sword",
	// 	Damage: 100.0,
	// 	Reach:  90.0,
	// 	Weight: 90.0,
	// }
	// damage := sword.Attack()
	// fmt.Printf("%s did %f damage.\n", sword.Name, damage)

	/*
		What happens if we define the struct with 0 values? It's nonsense.
		In other languages, we use constructors to fix this problem. Go doesn't have this.

		Instead in Go, if the zero value of a struct is unusable, you need to make that struct unexportable.
		If the package has only one struct, then you create a function called New  (exportable) that requires all the fields and returns back the struct.

	*/
	sword := weapon.New("Fury", "Sword", 100.0, 90.0, 90.0)
	damage := sword.Attack()
	fmt.Printf("%s did %f damage.\n", sword.Name, damage)

	/*
		Inheritance - there is none. We achieve this instead using Composition. This is where a struct references another struct.
		The armor struct references another struct called armorstats

		To avoid doing armor.armorstats.Defense, go makes it easy. Instead you can access Defense as if it were a primary attribute armor.Defense.
	*/
	armorstats := armor.NewArmorStats(10.0, 50.0)
	arm := armor.NewArmor("Iron Cuirass", armorstats)
	arm.PrintInfo()

	/*
		We can also have a slice of structs embedded within another struct.
		For example, something to hold all of our armors in the game.
	*/
	armorstats2 := armor.NewArmorStats(20.0, 25.0)
	arm2 := armor.NewArmor("Steel Helmet", armorstats2)
	inventory := armor.ArmorInventory{
		Armors: []armor.Armor{arm, arm2},
	}
	inventory.PrintArmorNames()

	/*
		Polymorphism - Refresher: the idea that something can have multiple forms.
		It comes in the form of interfaces, which conform to the same interface despite different underyling forms.
		IE: Squares, Circles, Rectangles, and Triangles are all Shapes and conform to the "interface" of a shape.

		In Go, an interface can hold any value that implements its interface

		For this project, lets consider an organization that's overall income comes from two different projects.
	*/
	// Both FixedBilling and TimeAndMaterial conform to the Income interface, despite different underlying structures
	project1 := income.FixedBilling{"Project 1", 5000}
	project2 := income.FixedBilling{"Project 2", 10000}
	project3 := income.TimeAndMaterial{"Project 3", 160, 25}
	incomeStreams := []income.Income{project1, project2, project3}
	income.CalculateNetIncome(incomeStreams)

	// If we wanted to add a new income stream, the interface has made this easier. We implement each method of the interface, and it works
	// Ideally, the functions that act on the interface itself do not change - the underlying methods abstract those things away

}

func simpleDefer1() {
	fmt.Println("Finished")
}

func simpleDefer() {
	defer simpleDefer1() // despite being at the top, this will be the last line run
	fmt.Println("Started")
}

type rect struct {
	length int
	width  int
}

func (r rect) area(wg *sync.WaitGroup) {
	if r.length < 0 {
		fmt.Printf("rect %v's length should be greater than zero\n", r)
		wg.Done()
		return
	}
	if r.width < 0 {
		fmt.Printf("rect %v's width should be greater than zero\n", r)
		wg.Done()
		return
	}
	area := r.length * r.width
	fmt.Printf("rect %v's area %d\n", r, area)
	wg.Done()
}

func (r rect) area1(wg *sync.WaitGroup) {
	defer wg.Done()
	if r.length < 0 {
		fmt.Printf("rect %v's length should be greater than zero\n", r)
		return
	}
	if r.width < 0 {
		fmt.Printf("rect %v's width should be greater than zero\n", r)
		return
	}
	area := r.length * r.width
	fmt.Printf("rect %v's area %d\n", r, area)
}

func deferStatement() {
	/*
		Defer is used when a function call should be executed irrespective of the code flow.
		It will be the last thing run inside the function, regardless of where it is placed
	*/
	// Simple example
	simpleDefer() // this will print Started and then Finished

	/*
		Some important things:
			- Defer can be run on methods
			- Arguments passed to defer are made when the defer statement is executed, NOT when the actual function is called
				-IE: If I pass in x = 1 to defer, increment 1 in the main function, and print in the defer function, it will print 1 not 2
			- If multiple defer statements are present in a function, they will be executed in LIFO order (stack)
	*/

	// Practical usage - look how complicated the above area function is - we keep having to call wg.Done() everywhere. Defer would be nice here...
	// Now look at area1 - see how much better that is. That's why you use defer.
}

func openFakeFile() {
	f, err := os.Open("file.txt") // notice how we use the same value, ok := syntax as usual
	if err != nil {               // err will be nil if things are ok.
		fmt.Println(err)
		return
	}
	fmt.Println(f.Name(), "opened successfully")
}

func openFakeFileBetter() {
	f, err := os.Open("test.txt")
	if err != nil {
		var pErr *os.PathError     // note how we define a PathError here
		if errors.As(err, &pErr) { // And then we test if the error raised was a Path Error
			fmt.Println("Failed to open file at path", pErr.Path) // Now we can access the full path to get a better error message
			return
		}
		fmt.Println("Generic error", err)
		return
	}
	fmt.Println(f.Name(), "opened successfully")
}

func dnsError() {
	addr, err := net.LookupHost("golangbot123.com")
	if err != nil {
		var dnsErr *net.DNSError //again we are checking for a specific error type
		if errors.As(err, &dnsErr) {
			if dnsErr.Timeout() { // these boolean functions that are provided tell us a lot more
				fmt.Println("operation timed out")
				return
			}
			if dnsErr.Temporary() {
				fmt.Println("temporary error")
				return
			}
			fmt.Println("Generic DNS error", err)
			return
		}
		fmt.Println("Generic error", err)
		return
	}
	fmt.Println(addr)
}

func directComparison() {
	files, err := filepath.Glob("[")
	if err != nil {
		if errors.Is(err, filepath.ErrBadPattern) { // very similar, we are just checking if the error is a specific type of error
			fmt.Println("Bad pattern error:", err)
			return
		}
		fmt.Println("Generic error:", err)
		return
	}
	fmt.Println("matched files", files)
}

func errorHandling() {
	// The idomatic way of handling errors is to check if the err is nil or not
	openFakeFile()

	// An error is simply an interface that defines a method called Error() which returns a string.
	/*
		How can we extract better information from an error?
		1 - We could convert the error to it's underlying type and get more info on the struct fields (ex: PathError)
		IE: PathErrors have three attributes: Op, Path, and Err.
	*/
	openFakeFileBetter()

	// 2 - Sometimes the underlying error methods have their own methods.
	// DNSError has two methods called Timeout() and Temporary() to let us know why the error exists.
	dnsError()

	// 3 - Direct comparison - You can check if an error is a type of error by comparing them directly
	directComparison()
}

func rectangleArea(side1 float64, side2 float64) (float64, error) {
	if side1 < 0 || side2 < 0 {
		return 0, simpleerror.New("Area calculation failed, side length is less than 0")
	}
	return side1 * side2, nil
}

func rectangleArea2(side1 float64, side2 float64) (float64, error) {
	if side1 < 0 || side2 < 0 {
		return 0, &rectangleerror.RectangleError{
			Err:   "at least one of the sides is negative",
			Side1: side1,
			Side2: side2,
		}
	}
	return side1 * side2, nil
}

func customErrors() {
	/*
		You can create really nice custom errors by taking advantage of:
			- The New Function
			- fmt.Errorf
			- Structs
			- Methods
	*/
	// Starting with a simple error
	// area, err := rectangleArea(-10, -20)
	// if err != nil {
	// 	fmt.Println(err)
	// 	return
	// }
	// fmt.Printf("Area of rectnagle %0.2f\n", area)

	// The more complicated RectangleError
	// Basically, we can take advantage of structs, methods, and the error interface to provide more custom error handling
	area1, err1 := rectangleArea2(-10, -20)
	if err1 != nil {
		var recError *rectangleerror.RectangleError
		if errors.As(err1, &recError) {
			if recError.Side1Negative() {
				fmt.Printf("error: side1 %f is less than zero\n", recError.Side1)
			}
			if recError.Side2Negative() {
				fmt.Printf("error: side2 %f is less than zero\n", recError.Side2)
			}
			return
		}
		fmt.Println(err1)
		return
	}
	fmt.Println("area of rect", area1)
}

func fullName(firstName *string, lastName *string) string {
	defer fmt.Println("deferred call in fullName")
	if firstName == nil {
		panic("First name ptr cannot be null")
	} else if lastName == nil {
		panic("Last name ptr cannot be null")
	}
	return *firstName + " " + *lastName
}

func deferedRecover() {
	fmt.Println("Deferred function")
	if r := recover(); r != nil {
		fmt.Println("Recovered", r)
	}
}

func selectBadSlice() {
	defer deferedRecover()
	numbers := make([]int, 5)
	fmt.Println(numbers[6])
}

// This function is directly called by addTwoNumbersThenDivideByX, thus the recover works
func divideNumbers(num int, den int) int {
	div := num / den
	fmt.Println(div)
	return div
}

func addTwoNumbersThenDivideByX(x int, y int) int {
	defer deferedRecover()
	sum := x + y
	return divideNumbers(sum, x)
}

// This function is a separate routine
// Even though it started by addTwoNumbersThenDivideByX2, the recover will not work
func divideNumbers2(num int, den int, ch chan int) {
	div := num / den
	fmt.Println(div)
	ch <- div
}

func addTwoNumbersThenDivideByX2(x int, y int) int {
	defer deferedRecover()
	sum := x + y
	ch := make(chan int)
	go divideNumbers2(sum, x, ch)
	return <-ch
}

func panics() {
	/*
		Using errors is the most idiomatic way to handle abnormal conditions. But sometimes, the program cannot continue after these conditions.
		Panic is used to prematurely end a program. When a panic is encountered, deferred functions are executed, and control returns to the caller
		This continues until all functions of the current program return at which point a panic is printed, stack trace, and termination.

		You can recover a panicking program with recover, covered later.

		When is the right time to use panic?
		1) An unrecoverable error means the program cannot continue
		2) Programmer errors - if we are expecting a pointer but we get Nil due to a programmer, we can panic.
	*/

	// Quick example - this will panic due to null pointer on the last name
	// firstName := "Elon"
	// fullName(&firstName, nil)
	// Deferred calls still happen during panics - you will notice above in the fullName function
	// deferred call in fullName is still printed

	// Panics happen at runtime, such as trying to access a slice with an index out of range
	// numbers := make([]int, 5)
	// fmt.Println(numbers[6])

	/*
		recover is a keyword that lets you regain control from a panic.
		It MUST be called within a deferred function. If it is outside, it will not be executed.
	*/
	// The defered function has a recover in it that recovers from a panic
	// selectBadSlice()

	// How do we get the stack trace off a recovered panic?
	// debug.PrintStack() // this function here prints the stack trace of the panic

	// You can recover a function if they are directly calling each other
	addTwoNumbersThenDivideByX(0, 10)

	// But you cannot if the functions are different goroutines (even if go was called from that function)
	// addTwoNumbersThenDivideByX2(0, 10)
}

func firstClassFunctions() {

}

func main() { // the main function should always reside in the main package
	// printHelloWorld()
	// printAge()
	// printWidthHeight()
	// printPersonInfo()
	// shorthandDeclaration()
	// typeConversions()
	// constants()
	// testDivision()
	// fmt.Println(funcWithParameters(15, 3))
	// fmt.Println(funcWithMultipleReturns(15, 3))
	// fmt.Println(returnNamedParameters(15, 3))
	// area, _ := returnNamedParameters(15, 3) // like python, we can use _ when we don't care about one of the return values
	// fmt.Println(area)
	// conditionals(10, 10)
	// conditionals(7, 10)
	// conditionals(5, 5)
	// assignment_if(10)
	// idiomatic_if(10)
	// loop_basic()
	// crazy_loop()
	// nested_labeled_loop()
	// printFinger(3)
	// fmt.Println("a is vowel: ", checkIsVowel("a"))
	// checkTruth(-2)
	// arrays()
	// slices()
	// _ = variadicNumFunction(10, 1, 2, 3, 5, 7, 9, 10, 11, 13)
	// maps()
	// strings()
	// pointers()
	// structs()
	// methods()
	// interfaces()
	// interfaces2()
	// concurrency()
	// goroutines()
	// channels()
	// bufferedChannels()
	// workerPools()
	// selectStatement()
	// mutexes()
	// oop()
	// deferStatement()
	// errorHandling()
	// customErrors()
	// panics()
	firstClassFunctions()
}

// Revisit: Strings, Packages
// Create cheat sheet
