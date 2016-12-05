#!/usr/bin/env python

def readinput():
  with open('input.txt') as f:
    text = f.readline().strip('\n')
  return text.split(', ')


def process_move(move, position, orientation, visited):
  if move[0] == 'R':
    orientation = (orientation + 1)%4
  elif move[0] == 'L':
    orientation = (orientation - 1 + 4)%4

 
  (x, y) = position
  if orientation == 0:
    x += int(move[1:])
    for i in range(position[0], x):
      visited.append((i + 1, y))
  elif orientation == 1:
    y += int(move[1:])
    for i in range(position[1], y):
      visited.append((x, i + 1))
  elif orientation == 2:
    x -= int(move[1:])
    for i in range(position[0], x, -1):
      visited.append((i - 1, y))
  elif orientation == 3:
    y -= int(move[1:])
    for i in range(position[1], y, -1):
      visited.append((x, i - 1))
  
  return ((x,y), orientation, visited)


def main():
  moves = readinput()
  position = (0,0)
  orientation = 0
  visited = [position]
  hq = None
  for move in moves:
    (position, orientation, visited) = process_move(move, position, orientation, visited)

  print "Puzzle 1:", abs(position[0]) + abs(position[1])

  print visited
  seen = []
  for pos in visited:
    if pos not in seen:
      seen.append(pos)
    else:
      hq = pos
      break
  print hq
  print "Puzzle 2:", abs(hq[0]) + abs(hq[1])



if __name__ == "__main__":
  main()
