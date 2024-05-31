from collections import deque
import math


listrowmaze = []
listcolmaze = []
fullmaze=[]
map={}
mappath={}
col = 0
rw = 0
class Node:
    id = None  # Unique value for each node.

    visit = False
    up = None  # Represents value of neighbors (up, down, left, right).
    down = None
    left = None
    right = None
    previousNode = None  # Represents value of neighbors.
    edgeCost = None  # Represents the cost on the edge from any parent to this node.
    gOfN = None  # Represents the total edge cost
    hOfN = None  # Represents the heuristic value
    heuristicFn = None  # Represents the value of heuristic function

    def __init__(self, value):
        self.value = value


class SearchAlgorithms:
    ''' * DON'T change Class, Function or Parameters Names and Order
        * You can add ANY extra functions,
          classes you need as long as the main
          structure is left as is '''
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    totalCost = -1  # Represents the total cost in case using UCS, AStar (Euclidean or Manhattan)
    maze=''
    cost=[]
    costH=[]

    def __init__(self, mazeStr, edgeCost=None):
        ''' mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node'''
        self.maze=mazeStr
        self.cost=edgeCost



    def load(self):
        global listrowmaze
        global listcolmaze
        global fullmaze
        global map

        count=0
        listrowmaze.clear()
        listcolmaze.clear()
        listnode=[]
        map.clear()
        fullmaze.clear()




        size=len(self.maze)

        for i in range(0,size):
            if(self.maze[i]==','):
                continue
            elif(self.maze[i]==' '):
                listrowmaze.append(listcolmaze.copy())
                listcolmaze.clear()
            else:
                listcolmaze.append(self.maze[i])
        listrowmaze.append(listcolmaze.copy())

        for r in range(0,len(listrowmaze)):
            listnode.clear()
            for c in range(0,len(listrowmaze[r])):
                nnode=Node(listrowmaze[r][c])
                nnode.id=count
                # nnode.name=listrowmaze[r][c]
                if self.cost!=None:
                    nnode.edgeCost=self.cost[count]


                if r+1 < len(listrowmaze):
                    nnode.down=count+len(listrowmaze[r])
                else:
                    nnode.down =None
                if r-1 >= 0:
                    nnode.top=count-len(listrowmaze[r])
                else:
                    nnode.top=None
                if c+1 < len(listrowmaze[r]):
                    nnode.right=count+1

                else:
                    nnode.right=None
                if c-1 >= 0:
                    nnode.left=count-1

                else:
                    nnode.left=None
                map[count]=nnode
                listnode.append(nnode)
                count+=1
            fullmaze.append(listnode.copy())




    def DFS(self):
        self.load()
        self.fullPath.clear()
        self.path.clear()
        s=[]
        for  i in range(0,len(fullmaze)):
            for j in range(0,len(fullmaze[i])):
                if fullmaze[i][j].value=='S':
                    start = fullmaze[i][j]
                    fullmaze[i][j].visit=True
                    break


        s.append(start)


        while s:
            start = s.pop(0)
            # print(start.id)
            if start.value=='E':
                self.fullPath.append(start.id)
                break;
            else:
                global il,ir,it,id,jl,jr,jt,jd
                for i in range(0, len(fullmaze)):
                    for j in range(0, len(fullmaze[i])):
                        if fullmaze[i][j].id == start.left:
                            il=i
                            jl=j
                        if fullmaze[i][j].id == start.right:
                            ir=i
                            jr=j
                        if fullmaze[i][j].id == start.down:
                            id=i
                            jd=j
                        if fullmaze[i][j].id == start.top:
                            it=i
                            jt=j
                s.reverse()


                if start.right != None:
                    if fullmaze[ir][jr].visit == False:
                        if fullmaze[ir][jr].value == '.' or fullmaze[ir][jr].value == 'E':
                            s.append(fullmaze[ir][jr])
                            fullmaze[ir][jr].visit = True
                if start.left != None:
                    if fullmaze[il][jl].visit == False:
                        if fullmaze[il][jl].value == '.' or fullmaze[il][jl].value == 'E':
                            s.append(fullmaze[il][jl])
                            fullmaze[il][jl].visit = True
                if start.down != None:
                    if fullmaze[id][jd].visit == False:
                        if fullmaze[id][jd].value == '.' or fullmaze[id][jd].value == 'E':
                            s.append(fullmaze[id][jd])
                            fullmaze[id][jd].visit = True
                if start.top != None:
                    if fullmaze[it][jt].visit == False:
                        if fullmaze[it][jt].value == '.' or fullmaze[it][jt].value == 'E':
                            s.append(fullmaze[it][jt])
                            fullmaze[it][jt].visit = True




                s.reverse()





                self.fullPath.append(start.id)


        return self.path, self.fullPath

    def BFS(self):
        self.load()
        mappath.clear()
        self.fullPath.clear()
        self.path.clear()
        opened=deque()
        listnode=[]
        for  i in range(0,len(fullmaze)):
            for j in range(0,len(fullmaze[i])):
                if fullmaze[i][j].value=='S':
                    start = fullmaze[i][j]
                    fullmaze[i][j].visit=True
                    break

        opened.append(start)

        while True:
            if len(opened)>0:
                start = opened.popleft()
            else:
                break
            if start.value=='E':
                self.fullPath.append(start.id)
                break;
            else:
                global il, ir, it, id, jl, jr, jt, jd
                for i in range(0, len(fullmaze)):
                    for j in range(0, len(fullmaze[i])):
                        if fullmaze[i][j].id == start.left:
                            il=i
                            jl=j
                        if fullmaze[i][j].id == start.right:
                            ir=i
                            jr=j
                        if fullmaze[i][j].id == start.down:
                            id=i
                            jd=j
                        if fullmaze[i][j].id == start.top:
                            it=i
                            jt=j
                if start.top != None:
                    if fullmaze[it][jt].visit == False:
                        if fullmaze[it][jt].value == '.' or fullmaze[it][jt].value == 'E':
                            opened.append(fullmaze[it][jt])
                            fullmaze[it][jt].visit = True
                if start.down != None:
                    if fullmaze[id][jd].visit == False:
                        if fullmaze[id][jd].value == '.' or fullmaze[id][jd].value == 'E':
                            opened.append(fullmaze[id][jd])
                            fullmaze[id][jd].visit = True
                if start.right != None:
                    if fullmaze[ir][jr].visit == False:
                        if fullmaze[ir][jr].value == '.' or fullmaze[ir][jr].value == 'E':
                            opened.append(fullmaze[ir][jr])
                            fullmaze[ir][jr].visit = True
                if start.left != None:
                    if fullmaze[il][jl].visit == False:
                        if fullmaze[il][jl].value == '.' or fullmaze[il][jl].value == 'E':
                            opened.append(fullmaze[il][jl])
                            fullmaze[il][jl].visit = True


                if start.right != None:
                   listnode.append(map.get(start.right))
                if start.left != None:
                   listnode.append(map.get(start.left))
                if start.top!=None:
                   listnode.append(map.get(start.top))
                if start.down!=None:
                   listnode.append(map.get(start.down))


                mappath[start]=listnode.copy()
                listnode.clear()
                self.fullPath.append(start.id)

        queue = []
        queue.append([map[0]])
        path2 = []
        while queue:

            path2 = queue.pop(0)
            node = path2[-1]
            if node.value == 'E':
                break
            for adjacent in mappath.get(node, []):
                new_path = list(path2)
                new_path.append(adjacent)
                queue.append(new_path)


        for i in range(0, len(path2)):
            self.path.append(path2[i].id)



        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        return self.path, self.fullPath

    def UCS(self):
        self.load()
        mappath.clear()
        self.fullPath.clear()
        self.path.clear()
        opened = []
        listnode = []
        global  node,start
        for  i in range(0,len(fullmaze)):
            for j in range(0,len(fullmaze[i])):
                if fullmaze[i][j].value=='S':
                    start = fullmaze[i][j]
                    fullmaze[i][j].visit=True
                    break
        opened.append(start)

        while True:
            if len(opened) > 0:
                node=opened[0]
                global k
                k = 0
                for i in range(1,len(opened)):
                    if node.edgeCost>opened[i].edgeCost:
                        node=opened[i]
                        k = i

                start = opened.pop(k)
            else:
                break
            if start.value == 'E':
                self.fullPath.append(start.id)
                listnode.append(start)
                break
            else:
                global il, ir, it, id, jl, jr, jt, jd
                for i in range(0, len(fullmaze)):
                    for j in range(0, len(fullmaze[i])):
                        if fullmaze[i][j].id == start.left:
                            il = i
                            jl = j
                        if fullmaze[i][j].id == start.right:
                            ir = i
                            jr = j
                        if fullmaze[i][j].id == start.down:
                            id = i
                            jd = j
                        if fullmaze[i][j].id == start.top:
                            it = i
                            jt = j
                if start.top != None:
                    if fullmaze[it][jt].visit == False:
                        if fullmaze[it][jt].value == '.' or fullmaze[it][jt].value == 'E':
                            opened.append(fullmaze[it][jt])
                            fullmaze[it][jt].visit = True
                            fullmaze[it][jt].previousNode = start.id
                if start.down != None:
                    if fullmaze[id][jd].visit == False:
                        if fullmaze[id][jd].value == '.' or fullmaze[id][jd].value == 'E':
                            opened.append(fullmaze[id][jd])
                            fullmaze[id][jd].visit = True
                            fullmaze[id][jd].previousNode = start.id
                if start.right != None:
                    if fullmaze[ir][jr].visit == False:
                        if fullmaze[ir][jr].value == '.' or fullmaze[ir][jr].value == 'E':
                            opened.append(fullmaze[ir][jr])
                            fullmaze[ir][jr].visit = True
                            fullmaze[ir][jr].previousNode = start.id
                if start.left != None:
                    if fullmaze[il][jl].visit == False:
                        if fullmaze[il][jl].value == '.' or fullmaze[il][jl].value == 'E':
                            opened.append(fullmaze[il][jl])
                            fullmaze[il][jl].visit = True
                            fullmaze[il][jl].previousNode = start.id
                self.fullPath.append(start.id)


        self.totalCost=0
        for i in range(0, len(fullmaze)):
            for j in range(0, len(fullmaze[i])):
                if fullmaze[i][j].id==self.fullPath[len(self.fullPath)-1]:
                    nnode=fullmaze[i][j]

        while True:
            if nnode.value == 'S':
                self.path.append(nnode.id)
                self.totalCost += nnode.edgeCost
                break
            else:
                self.path.append(nnode.id)
                self.totalCost +=nnode.edgeCost
                for i in range(0, len(fullmaze)):
                    for j in range(0, len(fullmaze[i])):
                        if fullmaze[i][j].id == nnode.previousNode:
                            nnode = fullmaze[i][j]

        (self.path).reverse()
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        return self.path, self.fullPath, self.totalCost

    def AStarEuclideanHeuristic(self):
        self.load()
        mappath.clear()
        self.fullPath.clear()
        self.path.clear()
        opened = []
        listnode = []
        global node, start,cal
        global ie,je
        for i in range(0, len(fullmaze)):
            for j in range(0, len(fullmaze[i])):
                if fullmaze[i][j].value == 'E':
                    ie=i
                    je=j

        global total
        for i in range(0, len(fullmaze)):
            for j in range(0, len(fullmaze[i])):
                total = math.sqrt(((ie - i) * (ie - i)) + ((je - j) * (je - j)))
                fullmaze[i][j].hOfN = total

        for i in range(0, len(fullmaze)):
            for j in range(0, len(fullmaze[i])):
                if fullmaze[i][j].value == 'S':
                    start = fullmaze[i][j]
                    fullmaze[i][j].visit = True
                    fullmaze[i][j].gOfN=0
                    break
        opened.append(start)

        while True:
            if len(opened) > 0:
                node = opened[0]
                global k
                k = 0
                for i in range(1, len(opened)):

                    if node.gOfN+node.hOfN > opened[i].gOfN+opened[i].hOfN:
                        node = opened[i]
                        k = i

                start = opened.pop(k)
            else:
                break
            if start.value == 'E':
                self.fullPath.append(start.id)
                listnode.append(start)
                break
            else:
                global il, ir, it, id, jl, jr, jt, jd
                for i in range(0, len(fullmaze)):
                    for j in range(0, len(fullmaze[i])):
                        if fullmaze[i][j].id == start.left:
                            il = i
                            jl = j
                        if fullmaze[i][j].id == start.right:
                            ir = i
                            jr = j
                        if fullmaze[i][j].id == start.down:
                            id = i
                            jd = j
                        if fullmaze[i][j].id == start.top:
                            it = i
                            jt = j
                if start.top != None:
                    if fullmaze[it][jt].value == '.' or fullmaze[it][jt].value == 'E':
                        if fullmaze[it][jt].visit == False:
                            opened.append(fullmaze[it][jt])
                            fullmaze[it][jt].visit = True
                            fullmaze[it][jt].previousNode = start.id
                            fullmaze[it][jt].gOfN = start.edgeCost + fullmaze[it][jt].edgeCost
                        else:

                            cal = start.edgeCost + fullmaze[it][jt].edgeCost
                            if fullmaze[it][jt].gOfN > cal:
                                fullmaze[it][jt].gOfN = cal
                                for a in range(0,len(opened)):
                                    if opened[a].id==fullmaze[it][jt].id:
                                       opened[a].gofN=cal
                if start.down != None:
                    if fullmaze[id][jd].value == '.' or fullmaze[id][jd].value == 'E':
                        if fullmaze[id][jd].visit == False:
                            opened.append(fullmaze[id][jd])
                            fullmaze[id][jd].visit = True
                            fullmaze[id][jd].previousNode = start.id
                            fullmaze[id][jd].gOfN = start.edgeCost + fullmaze[id][jd].edgeCost

                        else:
                            cal = start.edgeCost + fullmaze[id][jd].edgeCost
                            if fullmaze[id][jd].gOfN > cal:
                                fullmaze[id][jd].gOfN = cal
                                for a in range(0,len(opened)):
                                    if opened[a].id==fullmaze[id][jd].id:
                                       opened[a].gOfN=cal
                if start.right != None:
                    if fullmaze[ir][jr].value == '.' or fullmaze[ir][jr].value == 'E':
                        if fullmaze[ir][jr].visit == False:
                            opened.append(fullmaze[ir][jr])
                            fullmaze[ir][jr].visit = True
                            fullmaze[ir][jr].previousNode = start.id
                            fullmaze[ir][jr].gOfN = start.edgeCost + fullmaze[ir][jr].edgeCost

                        else:
                            cal = start.edgeCost + fullmaze[ir][jr].edgeCost
                            if fullmaze[ir][jr].gOfN > cal:
                                fullmaze[ir][jr].gOfN = cal
                                for a in range(0,len(opened)):
                                    if opened[a].id==fullmaze[ir][jr].id:
                                       opened[a].gOfN=cal
                if start.left != None:
                    if fullmaze[il][jl].value == '.' or fullmaze[il][jl].value == 'E':
                        if fullmaze[il][jl].visit == False:
                            opened.append(fullmaze[il][jl])
                            fullmaze[il][jl].visit = True
                            fullmaze[il][jl].previousNode = start.id
                            fullmaze[il][jl].gOfN = start.edgeCost + fullmaze[il][jl].edgeCost


                        else:
                            cal = start.edgeCost + fullmaze[il][jl].edgeCost
                            if fullmaze[il][jl].gOfN > cal:
                                fullmaze[il][jl].gOfN = cal
                                for a in range(0,len(opened)):
                                    if opened[a].id==fullmaze[il][jl].id:
                                       opened[a].gOfN=cal
                self.fullPath.append(start.id)

        self.totalCost = 0
        for i in range(0, len(fullmaze)):
            for j in range(0, len(fullmaze[i])):
                if fullmaze[i][j].id == self.fullPath[len(self.fullPath) - 1]:
                    nnode = fullmaze[i][j]

        while True:
            if nnode.value == 'S':

                self.path.append(nnode.id)
                self.totalCost += nnode.edgeCost+.0
                break
            else:
                self.path.append(nnode.id)
                self.totalCost += nnode.edgeCost
                for i in range(0, len(fullmaze)):
                    for j in range(0, len(fullmaze[i])):
                        if fullmaze[i][j].id == nnode.previousNode:
                            nnode = fullmaze[i][j]



        (self.path).reverse()

        # Cost for a step is calculated based on edge cost of node
        # and use Euclidean Heuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        return self.path, self.fullPath, self.totalCost

    def AStarManhattanHeuristic(self):
        self.load()
        mappath.clear()
        self.fullPath.clear()
        self.path.clear()
        opened = []
        listnode = []
        global node, start
        global ie, je
        for i in range(0, len(fullmaze)):
            for j in range(0, len(fullmaze[i])):
                if fullmaze[i][j].value == 'E':
                    ie = i
                    je = j

        global total
        for i in range(0, len(fullmaze)):
            for j in range(0, len(fullmaze[i])):
                if fullmaze[i][j].value=='S':
                    fullmaze[i][j].edgeCost = 0
                else:
                    fullmaze[i][j].edgeCost = 1

                ii=(ie - i)
                if ii<0:
                    ii*=-1
                jj=(je - j)
                if jj<0:
                    jj*=-1
                total=ii+jj
                fullmaze[i][j].hOfN = total


        for i in range(0, len(fullmaze)):
            for j in range(0, len(fullmaze[i])):
                if fullmaze[i][j].value == 'S':
                    start = fullmaze[i][j]
                    fullmaze[i][j].visit = True
                    break
        opened.append(start)
        while True:
            if len(opened) > 0:
                node = opened[0]
                global k
                k = 0
                for i in range(1, len(opened)):

                    if node.gOfN+node.hOfN >opened[i].gOfN+opened[i].hOfN:
                        node = opened[i]
                        k = i

                start = opened.pop(k)
            else:
                break
            if start.value == 'E':
                self.fullPath.append(start.id)
                listnode.append(start)
                break
            else:
                global il, ir, it, id, jl, jr, jt, jd
                for i in range(0, len(fullmaze)):
                    for j in range(0, len(fullmaze[i])):
                        if fullmaze[i][j].id == start.left:
                            il = i
                            jl = j
                        if fullmaze[i][j].id == start.right:
                            ir = i
                            jr = j
                        if fullmaze[i][j].id == start.down:
                            id = i
                            jd = j
                        if fullmaze[i][j].id == start.top:
                            it = i
                            jt = j
                if start.top != None:
                    if fullmaze[it][jt].value == '.' or fullmaze[it][jt].value == 'E':
                        if fullmaze[it][jt].visit == False:
                            opened.append(fullmaze[it][jt])
                            fullmaze[it][jt].visit = True
                            fullmaze[it][jt].previousNode = start.id
                            fullmaze[it][jt].gOfN = start.edgeCost + fullmaze[it][jt].edgeCost

                        else:

                            cal = start.edgeCost + fullmaze[it][jt].edgeCost
                            if fullmaze[it][jt].gOfN > cal:
                                fullmaze[it][jt].gOfN = cal
                                # fullmaze[it][jt].previousNode = start.id
                                for a in range(0,len(opened)):
                                    if opened[a].id==fullmaze[it][jt].id:
                                       opened[a].gofN=cal
                                       # opened[a].previousNode = start.id
                if start.down != None:
                    if fullmaze[id][jd].value == '.' or fullmaze[id][jd].value == 'E':
                        if fullmaze[id][jd].visit == False:
                            opened.append(fullmaze[id][jd])
                            fullmaze[id][jd].visit = True
                            fullmaze[id][jd].previousNode = start.id
                            fullmaze[id][jd].gOfN = start.edgeCost + fullmaze[id][jd].edgeCost

                        else:
                            cal = start.edgeCost + fullmaze[id][jd].edgeCost
                            if fullmaze[id][jd].gOfN > cal:
                                fullmaze[id][jd].gOfN = cal
                                # fullmaze[id][jd].previousNode = start.id
                                for a in range(0, len(opened)):
                                    if opened[a].id == fullmaze[id][jd].id:
                                        # opened[a].previousNode = start.id
                                        opened[a].gOfN = cal

                if start.right != None:
                    if fullmaze[ir][jr].value == '.' or fullmaze[ir][jr].value == 'E':
                        if fullmaze[ir][jr].visit == False:
                            opened.append(fullmaze[ir][jr])
                            fullmaze[ir][jr].visit = True
                            fullmaze[ir][jr].previousNode = start.id
                            fullmaze[ir][jr].gOfN = start.edgeCost + fullmaze[ir][jr].edgeCost

                        else:
                            cal = start.edgeCost + fullmaze[ir][jr].edgeCost
                            if fullmaze[ir][jr].gOfN > cal:
                                fullmaze[ir][jr].gOfN = cal
                                for a in range(0,len(opened)):
                                    if opened[a].id==fullmaze[ir][jr].id:
                                       opened[a].gOfN=cal
                if start.left != None:
                    if fullmaze[il][jl].value == '.' or fullmaze[il][jl].value == 'E':
                        if fullmaze[il][jl].visit == False:
                            opened.append(fullmaze[il][jl])
                            fullmaze[il][jl].visit = True
                            fullmaze[il][jl].previousNode = start.id
                            fullmaze[il][jl].gOfN = start.edgeCost + fullmaze[il][jl].edgeCost


                        else:
                            cal = start.edgeCost + fullmaze[il][jl].edgeCost
                            if fullmaze[il][jl].gOfN > cal:
                                fullmaze[il][jl].gOfN = cal
                                for a in range(0,len(opened)):
                                    if opened[a].id==fullmaze[il][jl].id:
                                       opened[a].gOfN=cal


                self.fullPath.append(start.id)

        self.totalCost = 0
        for i in range(0, len(fullmaze)):
            for j in range(0, len(fullmaze[i])):
                if fullmaze[i][j].id == self.fullPath[len(self.fullPath) - 1]:
                    nnode = fullmaze[i][j]



        while True:
            if nnode.value == 'S':

                self.path.append(nnode.id)
                self.totalCost += nnode.edgeCost+.0
                break
            else:


                self.path.append(nnode.id)
                self.totalCost += nnode.edgeCost
                for i in range(0, len(fullmaze)):
                    for j in range(0, len(fullmaze[i])):
                        if fullmaze[i][j].id == nnode.previousNode:
                            nnode = fullmaze[i][j]



        (self.path).reverse()

        # Cost for a step is 1
        # and use ManhattanHeuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes

        return self.path, self.fullPath, self.totalCost


def main():
    s1 = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = s1.BFS()
    print('**BFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')
                #######################################################################################
    s2 = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = s2.DFS()
    print('**DFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')

                #######################################################################################


    s3 = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [0, 15, 2, 100, 60, 35, 30, 3
                                                                                                             , 100, 2, 15, 60, 100, 30, 2
                                                                                                             , 100, 2, 2, 2, 40, 30, 2, 2
                                                                                                             , 100, 100, 3, 15, 30, 100, 2
                                                                                                             , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = s3.UCS()
    print('** UCS **\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\nTotal Cost: ' + str(
        TotalCost) + '\n\n')
               #######################################################################################

    s4 = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [0, 15, 2, 100, 60, 35, 30, 3
                                                                                                             , 100, 2, 15, 60, 100, 30, 2
                                                                                                             , 100, 2, 2, 2, 40, 30, 2, 2
                                                                                                             , 100, 100, 3, 15, 30, 100, 2
                                                                                                             , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = s4.AStarEuclideanHeuristic()
    print('**ASTAR with Euclidean Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')

            #######################################################################################

    s5 = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath, TotalCost = s5.AStarManhattanHeuristic()
    print('**ASTAR with Manhattan Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')


main()