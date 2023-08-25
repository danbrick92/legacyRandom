package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

/*
	Worker Pools - a collection of threads that are waiting for tasks to be assigned to them
	Once they finish the task assigned, they make themselves available again for the next task.

	We will implement a worker pool using buffered channels.
	Our worker pool will carry out the task of finding the sum of a digits of the input number.
	For example if 234 is passed, the output would be 9 (2 + 3 + 4).
	The input to the worker pool will be a list of pseudo-random integers.

	The following are the core functionalities of our worker pool:
	- Creation of a pool of Goroutines which listen on an input buffered channel waiting for jobs to be assigned
	- Addition of jobs to the input buffered channel
	- Writing results to an output buffered channel after job completion
	- Read and print results from the output buffered channel
*/

// Start by defining our structs
type Job struct {
	id       int
	randomno int // the pseudo-random number
}
type Result struct {
	job         Job
	sumofdigits int // the sum of the digits
}

// Now we create buffered channels to receive jobs and save results
var jobs = make(chan Job, 10)
var results = make(chan Result, 10)

// Digits Function - calculates the sum of each digit
func digits(number int) int {
	sum := 0
	no := number
	for no != 0 {
		digit := no % 10
		sum += digit
		no /= 10
	}
	time.Sleep(2 * time.Second)
	return sum
}

// Now we create our worker
func worker(wg *sync.WaitGroup) {
	for job := range jobs { // goes through all the jobs we have looking for new jobs, and finds one
		output := Result{job, digits(job.randomno)} // when it finds one, it does the digits calc and stores Result
		results <- output                           // writes results
	}
	wg.Done() // Completed once all jobs are completed
}

// This function creates a pool of worker goroutines
func createWorkerPool(noOfWorkers int) {
	var wg sync.WaitGroup
	for i := 0; i < noOfWorkers; i++ {
		wg.Add(1)
		go worker(&wg)
	}
	wg.Wait() // the workers wont end until all jobs finished
	close(results)
}

// Allocates jobs to workers
func allocate(noOfJobs int) {
	for i := 0; i < noOfJobs; i++ { // for each job
		randomno := rand.Intn(999) // create a random int
		job := Job{i, randomno}    // create a new Job with that int
		jobs <- job                // put on the job channel
	}
	close(jobs) // finish off the jobs channel
}

// Simply reads off results
func result(done chan bool) {
	for result := range results {
		fmt.Printf("Job id %d, input random no %d , sum of digits %d\n", result.job.id, result.job.randomno, result.sumofdigits)
	}
	done <- true
}

func main() {
	startTime := time.Now()
	noOfJobs := 100
	go allocate(noOfJobs)
	done := make(chan bool)
	go result(done)
	noOfWorkers := 50 // increasing the number of workers makes this all much faster
	// IE: 10 = 20 seconds. 50 = 4 seconds
	createWorkerPool(noOfWorkers)
	<-done
	endTime := time.Now()
	diff := endTime.Sub(startTime)
	fmt.Println("total time taken ", diff.Seconds(), "seconds")
}

/*
	A Summary:
	1) We create jobs and results. jobs are tasks to be done by workers, and results are completed tasks
	2) We, in a multi-threaded way, begin creating n number of jobs
	3) At the same time, create the done channel which tracks when all jobs are done
	4) After 3 but at the same time as 2, we run result routine which constantly prints results out
	5) At the same time, we create our worker pools. These create m number of workers
	6) Each worker polls the jobs from 2, calculate, and feed results back into results channel.
	   The worker ends itself when the jobs end
	7) The worker pool ends when all its workers end
	8) Once 2 is done and 7 is done, we are done.
*/
