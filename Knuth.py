""" Jesse Martinez
    HW #1
"""

from math import sqrt, floor, factorial
from collections import deque
from numbers import Integral

maxFac = 200
maxRoot = pow(10,300)

"Runs a Breadth First Search with the given goal"
def bfs(goal):
	Q = deque()
	parents = {}
	parents[4] = None
	Q.append(4)
	
	while len(Q) != 0 and Q[0] != goal:
		parent = Q.popleft()
		for successor in successors(parent):
			if successor not in parents:
				parents[successor] = parent
				Q.append(successor)
			if successor == goal:
				parents[successor] == parent
	
	if(goal in parents):
		print(createPath(parents, goal))
	else:
		print("Path could not be found")

"Constructs the path of numbers from 4 to goal value"
def createPath(history, goal):
	path = deque()
	if history[goal] != None:
		path.append(goal)
		parent = history[goal]
		while parent != None:
			path.appendleft(parent)
			parent = history[parent]
	return path

"Generates a list of successors using sqrt, floor and factorial if possible"
def successors(parent):
	successors = deque()
	if isinstance(parent, (int,Integral)):
		if parent <= maxFac: 
			successors.append(factorial(parent))
	else:
		successors.append(floor(parent))

	if parent <= maxRoot:
		successors.append(sqrt(parent))
	
	return successors

if __name__ == "__main__":
	bfs(int(input("Input number:")))
