Written by: J. Asher Glover
Problem: The Pancake Problem

Run script: python3 pancake.py
EC Run script: python3 dijkstra.py

Input: Enter the order of the pancakes all on one line separated by spaces (Must enter a stack
	greater than 3 pancakes)

Structure: For each state I created a class called MyNode which holds a list which is the
	current state. It also holds a copy of the state of its parent node so that the solution
	path can be traced back by using the visited list. It also holds an integer which is the
	cost of getting to that specific state.  Cost in the sense of this function is the number
	of pancakes flipped in order to get from the start state to that state plus the number of pancakes
	that are still out of order.  There are also lists for the frontier which is all the children nodes 
	that have still yet to be explored and a visited list which is all the nodes that have already been 
	expanded.

Methodology:
	Main reads in the the stack of the pancakes splits it into a list of characters and
	transfers it to numMake to turn it into a list of integers and will then send the list
	to the aStar function.  The aStar function initializes the frontier with that first
	inputList as the start state of the program.  Then we pop that node and check if there
	are any gaps in the stack of of 2 sizes or greater. If there are then we create separate
	children by flipping the stack at each of those gaps separately.  From there we check to
	see if the child node has either already been visited and expanded or has already been
	entered into the frontier from the expansion of a previous node.  If neither is true then
	we enter it into the frontier.  If it is already in the frontier but at a higher cost then
	we replace that higher cost child with the current one.  We continuously run these 
	operations while also comparing against the goal_state after popping each new node out of 
	the frontier to see if we are done.  Once the program has successfully reached the goal 
	state we move on to the solution function which prints out all the necessary nodes to 
	remake the path the program took in order to get from the start state to the goal state.
	We also print out the total number of possible states and the number of states we actually
	went through and expanded on in order to reach the goal state.

Extra Credit:
	I didn't realize it at first but my first implementation of this program was actually the Dijkstra
	version.  I say this because in my first version of this program I concatenated the parent's cost with
	the number of pancakes flipped to go from the parent to this current child as the cost for that child.
	However with the A* function I also have to consider the forward cost and not just the cost of the path.
	So therefore I added an additional cost which I deem as the forward cost because it tells you how many pancakes
	are still out of order.  So now when it picks the smallest cost it is not only considering the child that has
	the shortest path but also which child, on top of that, has the fewest pancakes still out of order.  Which means
	I kept my original implementation as the submission for the extra credit.