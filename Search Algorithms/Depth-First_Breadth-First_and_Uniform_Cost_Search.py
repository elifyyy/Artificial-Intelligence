
class node: #not keeping heuristic
    def __init__(self,i,j,value,parent,cost):
        self.i = i #node's row index at maze
        self.j = j #node's col index at maze
        self.value=value #node's additional movement points
        self.parent = parent #node's parent,initially empty
        self.cost = cost #total destinantion cost of the node



class nodeH: #keep heuristic too
    def __init__(self,i,j,value,parent,cost,heuristic):
        self.i = i #node's row index at maze
        self.j = j #node's col index at maze
        self.value=value #node's additional movement points
        self.parent = parent #node's parent,initially empty
        self.cost = cost #total destinantion cost of the node
        self.heuristic = heuristic




"""  I CREATE MAZES HARD CODED. NODE'S FIRST TWO ATTRIBUTES ARE INDEXES [İ][J] ([ROW][COL]). THIRD ATTRIBUTE IS VALUE WICH IS ADDITIONAL 
 MOVEMENT POINT FOR THAT NODE AND "-" IF IT IS A WALL. WE CAN CHANGE NODE'S VALUE BY CHANGING THIRD ATTRIBUTE OF THE OBJECT. 
 TO ADD NEW NODES PLEASE GIVE i AND j ATTRIBUTES CORRECTLY ACORRDING TO IT'S INDEX.GIVE ANY VALUE TO THIRD ATTRIBUTE OR GIVE "-" IF IT IS A WALL.
 PLASE GIVE FOURTH ATTRIBUTE(PARENT) AS "", PARENT WILL BE SET LATER.(HANGI NODEUN EXPLORE EDİLMESİYLE ULAŞILMIŞSA O NODE PARETN OLARAK SET EDİLECEK).
 """


maze = [ [node(0,0,"-","",0),node(0,1,0,"",0),node(0,2,1,"",0),node(0,3,0,"",0),node(0,4,1,"",0)],
         [node(1, 0,"-","",0), node(1, 1,"-","",0), node(1, 2,2,"",0), node(1, 3,1,"",0), node(1, 4,2,"",0)],
         [node(2, 0,2,"",0), node(2, 1,"-","",0), node(2, 2,3,"",0), node(2, 3,0,"",0), node(2, 4,"-","",0)],
         [node(3, 0,0,"",0), node(3, 1,2,"",0), node(3, 2,1,"",0), node(3, 3,1,"",0), node(3, 4,"-","",0)],
         [node(4, 0,1,"",0), node(4, 1,0,"",0), node(4, 2,3,"",0), node(4, 3,1,"",0), node(4, 4,"-","",0)] ]




#last attribute of node is heuristic.First heuristics are inadmissiable,they are much bigger than real cost.
# I calculate heurisctic in calculate heuristic() method.We i call a_star_search(maze) method, i transform maze into a maze with admissable heuristics.At line 388
# I explain it in report.

maze_inadmissable_heuristic = [ [nodeH(0,0,"-","",0,1000),nodeH(0,1,0,"",0,700),nodeH(0,2,1,"",0,700),nodeH(0,3,0,"",0,700),nodeH(0,4,1,"",0,700)],
                             [nodeH(1, 0,"-","",0,7000), nodeH(1, 1,"-","",0,7000), nodeH(1, 2,2,"",0,700), nodeH(1, 3,1,"",0,7), nodeH(1, 4,2,"",0,700)],
                             [nodeH(2, 0,2,"",0,700), nodeH(2, 1,"-","",0,117), nodeH(2, 2,3,"",0,7000), nodeH(2, 3,0,"",0,7), nodeH(2, 4,"-","",0,700)],
                             [nodeH(3, 0,0,"",0,700), nodeH(3, 1,2,"",0,700), nodeH(3, 2,1,"",0,7000), nodeH(3, 3,1,"",0,227), nodeH(3, 4,"-","",0,7000)],
                             [nodeH(4, 0,1,"",0,700), nodeH(4, 1,0,"",0,700), nodeH(4, 2,3,"",0,7000), nodeH(4, 3,1,"",0,7000), nodeH(4, 4,"-","",0,700)] ]





def calculate_heuristic(maze,goal_node):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            current_node = maze[i][j]
            heuristic = abs(abs(goal_node.i-current_node.i)*abs(goal_node.i-current_node.i) - abs(goal_node.j-current_node.j)*abs(goal_node.j-current_node.j))
            if(current_node.value!="-"):
                heuristic = heuristic +current_node.value
            if(goal_node.value!="-"):
                heuristic = heuristic + goal_node.value
            current_node.heuristic = int(heuristic)
            maze[i][j]=current_node
    return maze



def bread_first_search(maze,initial_node,goal_node):
    frontier_queue = []
    explored_array =[]
    path = []
    frontier_queue.append(initial_node)#enqueue initial node
    not_found = True
    while(not_found):
        explored_array.append(frontier_queue[0])
        frontier_queue.remove(frontier_queue[0]) #dequeue
        if(explored_array[-1]==goal_node):
            not_found = False
            temp_node = goal_node
            while (temp_node is not None and temp_node.parent != ""):
                path.append((temp_node.parent.i, temp_node.parent.j))  # back track, list is reverse order
                temp_node = temp_node.parent
            path = path[::-1]  # reverse the list to get the correct order
            path.append((goal_node.i, goal_node.j))  # add goal node at the end
        else :
            # keep indexes of added elem to explored array for finding new frontiers.
            i = explored_array[-1].i
            j = explored_array[-1].j

            # add frontier queue in this order :   check up/check below/check left/check right
            if ((i - 1) > 0):
                if ((maze[i - 1][j] not in frontier_queue) and (maze[i-1][j] not in explored_array)and maze[i - 1][j].value != "-"):  # check if it is already exist in the queue and if it is a wall or not.
                    frontier_queue.append(maze[i - 1][j])
                    maze[i - 1][j].parent = [1]  # set parent node, last expolered node is the parent of new frointiers nodes
            if ((i + 1) <= (len(maze)-1)):
                if ((maze[i + 1][j] not in frontier_queue) and (maze[i+1][j] not in explored_array) and maze[i + 1][j].value != "-"):
                    frontier_queue.append(maze[i + 1][j])
                    maze[i + 1][j].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes

            if ((j - 1) > 0):
                if ((maze[i][j - 1] not in frontier_queue)and (maze[i][j-1] not in explored_array) and maze[i][j - 1].value != "-"):
                    frontier_queue.append(maze[i][j - 1])
                    maze[i][j-1].parent = explored_array[-1]   # set parent node, last expolered node is the parent of new frointiers nodes


            if ((j + 1) <= len(maze[0]) - 1):
                if ((maze[i][j + 1] not in frontier_queue) and (maze[i][j+1] not in explored_array)and maze[i][j + 1].value != "-"):
                    frontier_queue.append(maze[i][j + 1])
                    maze[i][j+1].parent = explored_array[-1]   # set parent node, last expolered node is the parent of new frointiers nodes

        if (len(frontier_queue) == 0):
            print("not found")
            break
    return (path,explored_array)





def depth_first_search(maze,initial_node,goal_node):
    frontier_stack = []
    explored_array =[]
    path =[]
    frontier_stack.append(initial_node)#push initial node
    not_found = True
    while(not_found):
        explored_array.append(frontier_stack.pop())
        if(explored_array[-1]==goal_node):
            not_found = False
            temp_node = goal_node
            print("path:")
            while (temp_node is not None and temp_node.parent != ""):
                path.append((temp_node.parent.i, temp_node.parent.j))  # back track, list is reverse order
                temp_node = temp_node.parent
            path = path[::-1]  # reverse the list to get the correct order
            path.append((goal_node.i, goal_node.j))  # add goal node at the end

        else :
            # keep indexes of added elem to explored array for finding new frontiers.
            i = explored_array[-1].i
            j = explored_array[-1].j

            # add frontier stack in this order :   check up/check below/check left/check right
            if ((i - 1) > 0):
                if ((maze[i - 1][j] not in frontier_stack)and (maze[i - 1][j] not in explored_array) and maze[i - 1][j].value != "-"):  # check if it is already exist in the queue and if it is a wall or not.
                    frontier_stack.append(maze[i - 1][j])
                    maze[i - 1][j].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes

            if ((i + 1) <= (len(maze)-1)):
                if ((maze[i + 1][j] not in frontier_stack) and(maze[i + 1][j] not in explored_array) and maze[i + 1][j].value != "-"):
                    frontier_stack.append(maze[i + 1][j])
                    maze[i + 1][j].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes

            if ((j - 1) > 0):
                if ((maze[i][j - 1] not in frontier_stack)and (maze[i][j-1] not in explored_array) and maze[i][j - 1].value != "-"):
                    frontier_stack.append(maze[i][j - 1])
                    maze[i][j - 1].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes

            if ((j + 1) <= len(maze[0]) - 1):
                if ((maze[i][j + 1] not in frontier_stack) and (maze[i][j+1] not in explored_array) and maze[i][j + 1].value != "-"):
                    frontier_stack.append(maze[i][j + 1])
                    maze[i][j + 1].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes
        if (len(frontier_stack) == 0):
            print("not found")
            break

    return (path,explored_array)


def uniform_cost_search_extra_points(maze,initial_node,goal_node):
    frontier_queue = []
    explored_array = []
    path = []
    frontier_queue.append(initial_node)  # enqueue initial node
    not_found = True
    while (not_found): # (dequeue minumum cost node from frontier / add it to expolerd list / find the children of explored node,calculate their cost / enqueue these childeren to frontier queue) loop until goal node is found
        # To sort the list in place...
        frontier_queue.sort(key=lambda x: x.cost, reverse=False)
        # To return a new list, use the sorted() built-in function...
        frontier_queue = sorted(frontier_queue, key=lambda x: x.cost, reverse=False) #node with minimum cost is always first elem
        explored_array.append(frontier_queue[0])
        frontier_queue.remove(frontier_queue[0])  # dequeue
        if (explored_array[-1] == goal_node):
            not_found = False
            temp_node = goal_node
            while (temp_node is not None and temp_node.parent != ""):
                path.append((temp_node.parent.i, temp_node.parent.j))  # back track, list is reverse order
                temp_node = temp_node.parent
            path = path[::-1]  # reverse the list to get the correct order
            path.append((goal_node.i, goal_node.j))  # add goal node at the end
        else:
            # keep indexes of added elem to explored array for finding new frontiers.
            i = explored_array[-1].i
            j = explored_array[-1].j

            # add frontier queue in this order :   check up/check below/check left/check right
            if ((i - 1) > 0):
                if ( (maze[i - 1][j] not in explored_array) and maze[i - 1][j].value != "-"):  # check if it is already exist in the queue and if it is a wall or not.
                    maze[i - 1][j].cost = explored_array[-1].cost + maze[i - 1][j].value +1 #add 1 as movement cost and additional cost for destination node
                    frontier_queue.append(maze[i - 1][j])
                    maze[i - 1][j].parent = explored_array[- 1]  # set parent node, last expolered node is the parent of new frointiers nodes
            if ((i + 1) <= (len(maze) - 1)):
                if ( ( maze[i+1][j] not in explored_array) and maze[i + 1][j].value != "-"):
                    maze[i + 1][j].cost = explored_array[-1].cost + maze[i+1][j].value +1 #add 1 as movement cost and additional cost for destination node
                    frontier_queue.append(maze[i + 1][j])
                    maze[i + 1][j].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes

            if ((j - 1) > 0):
                if ((maze[i][j - 1] not in explored_array) and maze[i][j - 1].value != "-"):
                    maze[i][j-1].cost = explored_array[-1].cost + maze[i][j-1].value+1 #add 1 as movement cost and additional cost for destination node
                    frontier_queue.append(maze[i][j - 1])
                    maze[i][j - 1].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes

            if ((j + 1) <= len(maze[0]) - 1):
                if ((maze[i][j + 1] not in explored_array) and maze[i][j + 1].value != "-"):
                    maze[i][j+1].cost = explored_array[-1].cost + maze[i][j+1].value +1 #add 1 as movement cost and additional cost for destination node
                    frontier_queue.append(maze[i][j + 1])
                    maze[i][j + 1].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes

        if(len(frontier_queue)==0):
            print("not found")
            break

    return(path,explored_array)





def uniform_cost_search_equal_points(maze,initial_node,goal_node):
    frontier_queue = []
    explored_array = []
    path = []
    frontier_queue.append(initial_node)  # enqueue initial node
    not_found = True
    while (not_found):# (dequeue minumum cost node from frontier / add it to expolerd list / find the children of explored node,calculate their cost / enqueue these childeren to frontier queue) loop until goal node is found
        # To sort the list in place...
        frontier_queue.sort(key=lambda x: x.cost, reverse=False)
        # To return a new list, use the sorted() built-in function...
        frontier_queue = sorted(frontier_queue, key=lambda x: x.cost,reverse=False)  #node with minimum cost is always first elem
        explored_array.append(frontier_queue[0])
        frontier_queue.remove(frontier_queue[0])  #dequeue
        if (explored_array[-1] == goal_node):
            not_found = False
            temp_node = goal_node
            while (temp_node is not None and temp_node.parent != ""):
                path.append((temp_node.parent.i, temp_node.parent.j))  #back track, list is reverse order
                temp_node = temp_node.parent
            path = path[::-1]  # reverse the list to get the correct order
            path.append((goal_node.i, goal_node.j))  # add goal node at the end
        else:
            # keep indexes of added elem to explored array for finding new frontiers.
            i = explored_array[-1].i
            j = explored_array[-1].j
            # add frontier queue in this order :   check up/check below/check left/check right
            if ((i - 1) > 0):
                if ((maze[i - 1][j] not in explored_array) and maze[i - 1][j].value != "-"):  # check if it is already exist in the queue and if it is a wall or not.
                    maze[i - 1][j].cost = explored_array[-1].cost  + 1  # add 1 as movement cost and additional cost for destination node
                    frontier_queue.append(maze[i - 1][j])
                    maze[i - 1][j].parent = explored_array[- 1]  # set parent node, last expolered node is the parent of new frointiers nodes
            if ((i + 1) <= (len(maze) - 1)):
                if ((maze[i + 1][j] not in explored_array) and maze[i + 1][j].value != "-"):
                    maze[i + 1][j].cost = explored_array[-1].cost +  1  # add 1 as movement cost and additional cost for destination node
                    frontier_queue.append(maze[i + 1][j])
                    maze[i + 1][j].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes

            if ((j - 1) > 0):
                if ((maze[i][j - 1] not in explored_array) and maze[i][j - 1].value != "-"):
                    maze[i][j - 1].cost = explored_array[-1].cost  + 1  # add 1 as movement cost and additional cost for destination node
                    frontier_queue.append(maze[i][j - 1])
                    maze[i][j - 1].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes

            if ((j + 1) <= len(maze[0]) - 1):
                if ((maze[i][j + 1] not in explored_array) and maze[i][j + 1].value != "-"):
                    maze[i][j + 1].cost = explored_array[-1].cost + 1  # add 1 as movement cost and additional cost for destination node
                    frontier_queue.append(maze[i][j + 1])
                    maze[i][j + 1].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes
        if (len(frontier_queue) == 0):
            print("not found")
            break
    return (path, explored_array)



def A_star_search(maze,initial_node,goal_node):
    frontier_queue = []
    explored_array = []
    path = []
    frontier_queue.append(initial_node)  #enqueue initial node
    not_found = True
    while (not_found):# (dequeue minumum cost node from frontier / add it to expolerd list / find the children of explored node,calculate their cost / enqueue these childeren to frontier queue) loop until goal node is found
        # To sort the list in place...
        frontier_queue.sort(key=lambda x: x.cost, reverse=False)
        # To return a new list, use the sorted() built-in function...
        frontier_queue = sorted(frontier_queue, key=lambda x: x.cost, reverse=False) #node with minimum cost is always first elem
        explored_array.append(frontier_queue[0])
        frontier_queue.remove(frontier_queue[0])  # dequeue
        if (explored_array[-1] == goal_node):
            not_found = False
            temp_node = goal_node
            while (temp_node is not None and temp_node.parent != ""):
                path.append((temp_node.parent.i, temp_node.parent.j))  # back track, list is reverse order
                temp_node = temp_node.parent
            path = path[::-1]  # reverse the list to get the correct order
            path.append((goal_node.i, goal_node.j))  # add goal node at the end


        else:
            # keep indexes of added elem to explored array for finding new frontiers.
            i = explored_array[-1].i
            j = explored_array[-1].j
            if ((i - 1) > 0):
                if ( (maze[i - 1][j] not in explored_array) and maze[i - 1][j].value != "-"):  # check if it is already exist in the queue and if it is a wall or not.
                    maze[i - 1][j].cost = (explored_array[-1].cost- explored_array[-1].heuristic)+ maze[i - 1][j].value +1 + maze[i-1][j].heuristic  #add 1 as movement cost and additional cost for destination node
                    #(explored_array[-1].cost- explored_array[-1].herustic --> because i only want to add parent node's path cost and child node's heuristic and child node's path cost.Not parent node' heuristic too.
                    frontier_queue.append(maze[i - 1][j])
                    maze[i - 1][j].parent = explored_array[- 1]  # set parent node, last expolered node is the parent of new frointiers nodes
            if ((i + 1) <= (len(maze) - 1)):
                if ( ( maze[i+1][j] not in explored_array) and maze[i + 1][j].value != "-"):
                    maze[i + 1][j].cost = (explored_array[-1].cost - explored_array[-1].heuristic)+ maze[i+1][j].value +1 +maze[i+1][j].heuristic #add 1 as movement cost and additional cost for destination node
                    #(explored_array[-1].cost- explored_array[-1].herustic --> because i only want to add parent node's path cost and child node's heuristic and child node's path cost.Not parent node' heuristic too.
                    frontier_queue.append(maze[i + 1][j])
                    maze[i + 1][j].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes

            if ((j - 1) > 0):
                if ((maze[i][j - 1] not in explored_array) and maze[i][j - 1].value != "-"):
                    maze[i][j-1].cost = (explored_array[-1].cost- explored_array[-1].heuristic) + maze[i][j-1].value+1+maze[i][j-1].heuristic#add 1 as movement cost and additional cost for destination node
                    #(explored_array[-1].cost- explored_array[-1].herustic --> because i only want to add parent node's path cost and child node's heuristic and child node's path cost.Not parent node' heuristic too.
                    frontier_queue.append(maze[i][j - 1])
                    maze[i][j - 1].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes

            if ((j + 1) <= len(maze[0]) - 1):
                if ((maze[i][j + 1] not in explored_array) and maze[i][j + 1].value != "-"):
                    maze[i][j+1].cost = (explored_array[-1].cost- explored_array[-1].heuristic) + maze[i][j+1].value +1+maze[i][j+1].heuristic #add 1 as movement cost and additional cost for destination node
                    #(explored_array[-1].cost- explored_array[-1].herustic --> because i only want to add parent node's path cost and child node's heuristic and child node's path cost.Not parent node' heuristic too.
                    frontier_queue.append(maze[i][j + 1])
                    maze[i][j + 1].parent = explored_array[-1]  # set parent node, last expolered node is the parent of new frointiers nodes
        if (len(frontier_queue) == 0):
            print("not found")
            break
    return (path, explored_array)


#Print BFS
print("BFS")
path_bfs,explored_bfs = bread_first_search(maze,maze[0][0],maze[4][2])
print("All expolered nodes for BFS:")
temp=[]
for i in range(0,len(explored_bfs)):
    temp.append((explored_bfs[i].i,explored_bfs[i].j))
print(temp)
print("path:")
print(path_bfs)

print("****************************")

#Print DFS
print("DFS")
path_dfs,explored_dfs = depth_first_search(maze,maze[0][0],maze[4][2])
print("All expolered nodes for DFS:")
temp=[]
for i in range(0,len(explored_dfs)):
    temp.append((explored_dfs[i].i,explored_dfs[i].j))
print(temp)
print("path:")
print(path_dfs)

print("****************************")

#Print UCS with extra movement points
print("UCS with extra movement points")
path_ucs_ex,explored_ucs_ex= uniform_cost_search_extra_points(maze,maze[0][0],maze[4][2])
print("All expolered nodes for UCS with equal movement points:")
temp=[]
for i in range(0,len(explored_ucs_ex)):
    temp.append((explored_ucs_ex[i].i,explored_ucs_ex[i].j))
print(temp)
print("path:")
print(path_ucs_ex)


print("****************************")

#Print UCS with equal movement points
print("UCS with equal movement points")
path_ucs_eq,explored_ucs_eq= uniform_cost_search_equal_points(maze,maze[0][0],maze[4][2])
print("All expolered nodes for UCS with equal movement points:")
temp=[]
for i in range(0,len(explored_ucs_eq)):
    temp.append((explored_ucs_eq[i].i,explored_ucs_eq[i].j))
print(temp)
print("path:")
print(path_ucs_eq)


print("****************************")

#Print A* Search with admissable heuristics
print("A* Search with admissable heuristics")
maze_admissable_heuristic=calculate_heuristic(maze_inadmissable_heuristic, maze_inadmissable_heuristic[4][2]) #maze with admissable heuristics are created.Second
                                                                                                              #second argumant is goal node,
                                                                                                             # if we want to change goal node in the maze while calling
                                                                                                             #the method,this argumant must be changed too,


path_a_ad,explored_a_ad= A_star_search(maze_admissable_heuristic,maze_admissable_heuristic[0][0],maze_admissable_heuristic[4][2])
temp=[]
for i in range(0,len(explored_a_ad)):
    temp.append((explored_a_ad[i].i,explored_a_ad[i].j))
print("All expolered nodes for A* Seach with admissable heuristics:")
print(temp)
print("path:")
print(path_a_ad)


#Print A*Search with inadmissable heuristics
print("A* Search with inadmissable heuristics")
path_a_iad,explored_a_iad= A_star_search(maze_inadmissable_heuristic,maze_inadmissable_heuristic[0][0],maze_inadmissable_heuristic[4][2])
print("All expolered nodes for A* Search with inadmissable heuristics points:")
temp=[]
for i in range(0,len(explored_a_iad)):
    temp.append((explored_a_iad[i].i,explored_a_iad[i].j))
print(temp)
print("path:")
print(path_a_iad)
