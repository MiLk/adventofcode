package main

import (
	"container/list"
	"fmt"
)

type Circle struct {
	placed *list.List
	marbles int
	currentMarble int
	currentPos *list.Element
}

func (c *Circle) Completed() bool {
	return c.currentMarble == c.marbles
}

func (c *Circle) Place() int {
	if c.currentMarble % 23 == 0 {
		c.Prev().Prev().Prev().Prev().Prev().Prev().Prev()
		toRemove := c.currentPos
		s := toRemove.Value.(int) + c.currentMarble
		c.Next()
		c.placed.Remove(toRemove)
		c.currentMarble += 1
		return s
	} else {
		c.Next()
		c.currentPos = c.placed.InsertAfter(c.currentMarble, c.currentPos)
		c.currentMarble += 1
		return 0
	}
}

func (c *Circle) Next() *Circle {
	if e := c.currentPos.Next(); e != nil {
		c.currentPos = e
	} else {
		c.currentPos = c.placed.Front()
	}
	return c
}

func (c *Circle) Prev() *Circle {
	if e := c.currentPos.Prev(); e != nil {
		c.currentPos = e
	} else {
		c.currentPos = c.placed.Back()
	}
	return c
}

func (c *Circle) Print() {
	fmt.Print("Circle: ")
	for el := c.placed.Front(); el != nil; el = el.Next() {
		fmt.Printf("%d ", el.Value)
	}
	fmt.Print("\n")
}

func NewCircle(last int) *Circle {
	c := Circle{
		placed: list.New(),
		marbles: last,
		currentMarble: 1,
	}
	c.placed.PushFront(0)
	c.currentPos = c.placed.Front()
	return &c
}

func main() {
	solve(424, 71482)
	solve(424, 71482*100)
}

func solve(players, last int) {
	scores := map[int]int{}
	circle := NewCircle(last)
	for currentPlayer := 0;!circle.Completed(); {
		s:= circle.Place()
		if s > 0 {
			scores[currentPlayer] += s
		}
		currentPlayer = (currentPlayer + 1) % players
	}
	max := 0
	for _, s := range scores {
		if s > max {
			max = s
		}
	}
	println(max)
}
