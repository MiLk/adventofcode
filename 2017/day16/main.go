package main

import (
	"log"
	"strconv"
	"strings"
	"fmt"
	"bytes"
	"io/ioutil"
)

func main() {
	err := mainE()
	if err != nil {
		log.Fatal(err)
	}
}

type instruction struct {
	T  string
	X  int
	A  int
	B  int
	As []byte
	Bs []byte
}

func getInstructions(inss []string) ([]instruction, error) {
	ins := []instruction{}
	for _, i := range inss {
		i = strings.TrimSpace(i)
		if i[0] == 's' {
			x, err := strconv.Atoi(i[1:])
			if err != nil {
				return nil, err
			}
			ins = append(ins, instruction{
				T: "s",
				X: x,
			})
		} else if i[0] == 'x' {
			s := strings.Split(i[1:], "/")
			a, err := strconv.Atoi(s[0])
			if err != nil {
				return nil, err
			}
			b, err := strconv.Atoi(s[1])
			if err != nil {
				return nil, err
			}
			ins = append(ins, instruction{
				T: "x",
				A: a,
				B: b,
			})
		} else if i[0] == 'p' {
			s := strings.Split(i[1:], "/")
			ins = append(ins, instruction{
				T:  "p",
				As: []byte(s[0]),
				Bs: []byte(s[1]),
			})
		}
	}
	return ins, nil
}

func mainE() error {
	input, err := ioutil.ReadFile("input.txt")
	if err != nil {
		return err
	}

	ins, err := getInstructions(strings.Split(string(input), ","))
	if err != nil {
		return err
	}

	state := []byte("abcdefghijklmnop")
	l := len(state)

	seen := []string{}

	n := 1000000000
	for j := 0; j < n; j++ {
		sstate := string(state)
		if len(seen) > 0 && sstate == seen[0] {
			fmt.Println(seen[n % j])
			return nil
		}
		seen = append(seen, sstate)

		for _, i := range ins {
			switch i.T {
			case "s":
				state = append(state[l-i.X:], state[:l-i.X]...)
			case "x":
				state[i.A], state[i.B] = state[i.B], state[i.A]
			case "p":
				a := bytes.Index(state, i.As)
				b := bytes.Index(state, i.Bs)
				state[a], state[b] = state[b], state[a]
			}
		}

		if j == 0 {
			fmt.Println(string(state))
		}
	}

	return nil
}
