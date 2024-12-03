package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"sort"
)

// Solver is a completely unnecessary interface for solving the problem
type Solver interface {
	Part1(input Input) uint
	Part2(input Input) uint
}

// Solution is the implementation of the Solver interface
type Solution struct{}

// Input is the base struct for the data
type Input struct {
	list1   []int
	list2   []int
	freqMap map[int]int
}

// ParseFile reads the file content and creates a NewInput
func ParseFile(path string) (Input, error) {
	file, err := os.Open(path)
	if err != nil {
		return Input{}, fmt.Errorf("opening input file: %w", err)
	}
	defer file.Close()
	return NewInput(file), nil
}

// NewInput parses an io.Reader instance and returns an Input
func NewInput(rdr io.Reader) Input {
	scanner := bufio.NewScanner(rdr)
	var left, right []int
	freq := make(map[int]int)
	
	var l, r int
	for scanner.Scan() {
		fmt.Sscanf(scanner.Text(), "%d %d", &l, &r)
		left = append(left, l)
		right = append(right, r)
		freq[r]++
	}
	return Input{left, right, freq}
}

// Part1 solves the first part of the problem
// It sorts both of the arrays and sums the difference between the same indexes
func (s Solution) Part1(input Input) uint {
	left := append([]int(nil), input.list1...)
	right := append([]int(nil), input.list2...)

	sort.Ints(left)
	sort.Ints(right)

	var total uint
	for i := range left {
		if left[i] > right[i] {
			total += uint(left[i] - right[i])
		} else {
			total += uint(right[i] - left[i])
		}
	}
	return total
}

// Part2 solves the second part of the problem
// It sums each element in the left list by the number of occurrences in the right list
func (s Solution) Part2(input Input) uint {
	var total uint
	for _, num := range input.list1 {
		total += uint(num * input.freqMap[num])
	}
	return total
}
