package salarycalc

import "fmt"

type SalaryCalculator interface {
	CalculateSalary() int
}

type Employee struct {
	Name        string
	Salary      int
	Performance int
}

type Contractor struct {
	name    string
	basepay int
}

type Freelancer struct {
	name        string
	hourlyRate  int
	hoursWorked int
}

func (e Employee) CalculateSalary() int {
	return e.Salary + e.Performance
}

func (c Contractor) CalculateSalary() int {
	return c.basepay
}

func (f Freelancer) CalculateSalary() int {
	return f.hourlyRate * f.hoursWorked * 52
}

func TotalExpense(s []SalaryCalculator) int {
	// See how we operate on the interface now without caring about the underlying ds
	expense := 0
	for _, v := range s {
		expense += v.CalculateSalary()
	}
	return expense
}

func main() {
	// Create three different workers
	dan := Employee{
		Name:        "dan",
		Salary:      50000,
		Performance: 10000,
	}
	jim := Contractor{
		name:    "jim",
		basepay: 75000,
	}
	erin := Freelancer{
		name:        "erin",
		hourlyRate:  40,
		hoursWorked: 40,
	}

	employees := []SalaryCalculator{dan, jim, erin} // ensure these types conform to the interface
	fmt.Println(TotalExpense(employees))
}
