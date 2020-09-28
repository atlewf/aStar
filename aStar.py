from Map import Map_Obj

#%%

class Node():
    def __init__(self, pos = None, parent = None):
        self.pos = pos
        self.parent = parent
        self.g = 0 #steps from start node
        self.h = 0 #heuristic
        self.f = 0 #cost total

    def __eq__(self, other): #overwrite equation operator, compare using position
        return self.pos == other.pos
        
    
    
def h(current_pos, goal_pos): #heuristic distance from node to goal
    return abs(current_pos[0]-goal_pos[0]) + abs(current_pos[1]-goal_pos[1])
      

#%%

def aStar(map_obj, moving_goal = False):
    opened = [] #untraversed
    closed = [] #traversed
    
    size_of_map = map_obj.str_map.shape #needed for size

    init_node = Node(map_obj.start_pos, None)
    opened.append(init_node)

    
    while len(opened)>0:
        #sort the nodes in open wrt cost f
        opened.sort(key = lambda node: node.f) #at the end of loop so that smallest total ost is first
        
        #choose node with lowest cost
        current_node = opened.pop(0)
        
        #add to closed list
        closed.append(current_node)

        [x, y] = current_node.pos #get position of current node in abbreviated form
        
        #Check if current node is at the goal position, and if so return the path
        if [x,y] == map_obj.goal_pos:
            path = []
            
            #work backwards through ancestors
            while current_node != init_node:
                path.append(current_node.pos) 
                current_node = current_node.parent
            path.append(init_node.pos)
            
            #current order of path is from last to first, need to reverse path
            return path[::-1]        
  
        #the 4 adjacent nodes (down, up, right, left)
        adjacent = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]

        for i in adjacent:
            
            #if new position is a wall, don't make it a node
            if map_obj.get_cell_value(i) == -1: 
                continue
            
            #if new position is outside of map, don't make it a node
            if (i[0]<0) or (i[0]>=size_of_map[0]) or (i[1]<0) or (i[1]>=size_of_map[1]): 
                continue
            
            #new position is a legal position, make a node
            new_node = Node(i, current_node)
    
            #add the cell cost to the new node
            #note that cell cost = 1 for all legal fields in task 1 and 2
            new_node.h = h(i, map_obj.goal_pos)
            new_node.g = new_node.parent.g + map_obj.get_cell_value(i)

            
            #update total cost
            new_node.f = new_node.g + new_node.h
            
            #check if new_node is in opened and if it already has a lower cost
            add = True
            for old_node in opened:
                if old_node == new_node and new_node.f >= old_node.f:
                    add = False
                    
            #if we do not find a better f in opened, add the new node to the list
            if add == True:
                opened.append(new_node)
                
        #for task 5 we have a moving goal, update the goal position by calling tick() every iteration
        if moving_goal == True:
                map_obj.goal_pos = map_obj.tick()
                
    return None #did not find any path
            

#%%
#Task 1
map1 = Map_Obj(1)
path = aStar(map1)
print ("Task 1: The shortest path is", path, "\n")
#%%

#%%
##Vizualize 
for i in path[1:]:
    map1.replace_map_values(i, 5, map1.goal_pos)
map1.show_map()
#%%
#Task 2
map2 = Map_Obj(2)
path2 = aStar(map2)
print("Task 2: The shortest path is", path2, "\n")

#%%
#Vizualise
for i in path2[1:]:
    map2.replace_map_values(i, 5, map2.goal_pos)
map2.show_map()


#%%
#Task 3
map3 = Map_Obj(3)
path3 = aStar(map3)    
print("Task 3: The shortest path is", path3, "\n")

#%%
#Vizualise
for i in path3[1:]:
        map3.replace_map_values(i, 5, map3.goal_pos)
map3.show_map()

#%%
#Task 4
map4 = Map_Obj(4)
map4.show_map()
path4 = aStar(map4)
print("Task 4: The shortest path is", path4, "\n")

#%%
#Vizualise
for i in path4[1:]:
        map4.replace_map_values(i, 5, map4.goal_pos)
map4.show_map()

#%%
#Task 5
map5 = Map_Obj(5)
path5 = aStar(map5, moving_goal = True)
print("Task 5: The shortest path is", path5, "\n")

#%%
#Vizualise
for i in path5[1:]:
        map5.replace_map_values(i, 5, map5.goal_pos)
map5.show_map()

            