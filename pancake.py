import sys
import time
import math

goal_state = []
rev = []

class MyNode:
    state = []
    cost = 0
    parent = []

def myFunc(node):
    return node.cost

def gapHuer(node, index):
    # Checks to see if the pancake above the current pancake is
    # more than just 1 size greater
    gapb = 0
    gapf = 0

    temp = MyNode()

    # Check to see if the stack is in complete reverse order because
    # the gap hueristic will not catch this since there would be no
    # gaps in the stack
    if (checkRev(node)):

        # If checkRev is true we know that the stack is in complete
        # reverse order therefore we signify that to the rest of the
        # program
        return "Rev"
            
    # As long as it is not the first index in the list then we will
    # check the size gap of the current pancake and the pancake above
    # this one in the stack.
    if index != 0:
        gapb = abs(node.state[index - 1] - node.state[index])
    
    # Check the size gap of the current pancake and the pancake below
    # this one in the stack.
    if index != (len(node.state) - 1):
        gapf = abs(node.state[index + 1] - node.state[index])
  
    # If the size differences is greater than 1 either above or below
    # we return true meaning the stack should be flipped at this point
    if (gapb > 1 or gapf > 1):
        return True
    
    # Means that there is no gap so there should be no flip
    return False

def forCost(currList):
    i = 0
    count = 0

    while i < len(currList):
        if i+1 != currList[i]:
            count += 1
        i+=1

    return count

def flipFunc(parent, index):
    # Will use these lines in order to bring
    # the targeted pancake to the top of the
    node = MyNode()

    # append the indexes leading up to the desired pancake
    newList = parent.state[:(index + 1)]

    # flip the pancakes leading up to the desired pancake
    newList.reverse()

    # append the remaining pancakes after the list
    newList += parent.state[(index + 1):]

    forcost = forCost(newList)
        
    # update the values of this new child state before returning
    node.state = newList
    node.parent = parent.state

    # key difference between A* and dijkstra search with the addition
    # of for cost only in the A* because that is our forward cost in this sense
    # because it tells us the number of pancakes that are still out of order
    node.cost = parent.cost + (index + 1) + forcost

    return node

def checkRev(node):
    if node.state == rev:
        return True
    return False

def aStar(inputList):
    goal = False
    node = MyNode()
    node.state = inputList
    frontier = []
    visited = []
    child = MyNode()
    visit = False
    i = 0
    index = 0
    x = 0
    
    # Initialize the frontier with the start state
    frontier.append(node)

    while goal == False:
        if (len(frontier) == 0):
            return "Failure"

        # pop the start state to begin with the search tree
        # and simultaneously put it into the visited list
        frontier.sort(key=myFunc)
        node = frontier.pop(0)
        visited.append(node)

        # If we have reached our goal then we return the visited list
        # and we can use this list in order to trace back the path
        # we took to get to the goal state
        if (node.state == goal_state):
            goal = True
            visited.append(node)
            return visited
        
        while i < len(inputList):

            # Checks to see if there is a gap at this index of the specified
            # state
            if (gapHuer(node, i)):

                # If there is a gap that means a child node can be generated
                # by flipping the stack at that index
                child = flipFunc(node, i)

                # Check to see if this certain state has already been visited
                it = 0
                while it < len(visited):

                    if (visited[it].state == child.state):
                        # Lets us know that this state has indeed been visited before
                        visit = True
                    it += 1

                # Signifies that the child is not in the visited list
                if (visit == False):
                    it = 0
                    while it < len(frontier):

                        # Checks to see if this child is already in the frontier
                        # at a higher cost
                        if (frontier[it].state == child.state):

                            if (frontier[it].cost > child.cost):
                                # if it is then we replace it with the new lower cost child
                                frontier.pop(it)
                                frontier.insert(it, child)
                                #lets us know that this child has been entered into the frontier
                            visit = True
                        it += 1   
                            
                        # Signifies that the child is also not in the frontier
                        # Meaning that it should be added to the frontier
                    if (visit == False):
                        frontier.append(child)

                visit = False
            i += 1

        i = 0

    return visited

def numMake(inputList):

    temp = []
    solution = []

    # Used to transform the char numbers into regular ints
    for num in inputList:
        temp.append(int(num))

    print(temp)
    print(" ")

    # recieves the visited list from aStar after the completion
    solution = aStar(temp)
    return solution

def solution(nodes):
    i = len(nodes)-1
    temp = []
    switch = MyNode()
    switch = nodes[i]
    while(switch.parent != []):
        temp.append(switch.state)
        for box in nodes:
            if box.state == switch.parent:
              
                switch = box
                
    temp.append(switch.state)
    temp.reverse()

    for box in temp:
        print(box)

def setGoal(length):
    i = 1

    while i <= length:
        goal_state.append(i)
        i += 1
    i -= 1
    while i > 0:
        rev.append(i)
        i -= 1

def main():
    
    inputList = []
    # Recieve the order of the pancakes from input
    inputList = input("Enter the order of the pancakes (separated by spaces): ").split()
    if (len(inputList) != 0):
        setGoal(len(inputList))     
    else:
        # Triggered if all 5 pancakes are not listed on the same line
        print("Please list the order of the pancakes")

    # Triggered if the pancakes are already in the desired order

    # Runs the time of the program to give accurate info on
    # running time of the sort. Starts after receiving valid input
    start = time.time()

    # Lists the current order of the pancakes before starting the sort 
    print("Current Order: ")
    nodes = numMake(inputList)

    end = time.time()
    print("Number of Nodes Visited")
    print(len(nodes))
    print("Number of Possible States: ")
    print(math.factorial(len(inputList)))
    print(" ")

    print("Solution: ")

    solution(nodes)

    print("Elapsed Time: ")
    print(end-start)

if __name__ == '__main__':
    main()
