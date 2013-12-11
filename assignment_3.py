## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## COP 4531: Complexity and Analysis of Data Structures and Algorithms
## Programming Assignment 3, Due Date - 12/10/2013 11:59 PM
## Assigned - 10/10/2013
##
## John Cyr - jrc11v
##
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from heapq import heapify, heappush, heappop

class PriorityQueue():
    def __init__(self):
        self.pq = []
        self.status = {}

    def add(self, value, priority=0):
        entry = [priority, value]
        self.status[value] = entry
        heappush(self.pq, entry)

    def pop(self):
        priority, value = heappop(self.pq)
        return (value, priority)

    def empty(self):
        return len(self.pq) == 0
            
    def printPQ(self):
        for x in self.pq:
            print x[1], ':', x[0], ''

    def get_p(self, value):
        if value in self.status:
            return self.status[value][0]
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def main():
    fileName = raw_input('Enter Filename: ')
    readFile = open(fileName)

    setMode = True
    
    data = []

    directed = ''
    
    for line in readFile:
        if line[0] != '#':
            if setMode:
                if line[0] == 'D':
                    print 'Directed', '\n'
                    directed = True
                elif line[0] == 'UD':
                    print 'Undirected', '\n'
                    directed = False
                setMode = False
            else:
                if directed:
                    temp = line.split()
                    data.append((temp[0], temp[1], int(temp[2])))
                else:
                    temp = line.split()
                    data.append((temp[0], temp[1], int(temp[2])))
                    data.append((temp[1], temp[0], int(temp[2])))

    Dijkstra(data)
    ShortestPath(data)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Dijkstra(data):
    print 'Dijkstra'

    inf = float('inf')
    
    vSet = set()

    for i in data:
        vSet.add(i[0])
        vSet.add(i[1])
    
    loop = True
    source = ''
    
    while loop:
        if source not in vSet:
            source = raw_input('Source : ')[0]
        else:
            loop = False

    adjDict = {vertex: set() for vertex in vSet} # dic w/ char key and sets of tuples

    for start, end, cost in data:
        adjDict[start].add((end, cost))

    data = PriorityQueue()

    for i in vSet:
        if i == source:
            data.add(i, 0)
        else:
            data.add(i, inf)

    uq = data.pop() # Pop min Starting node
        
    while(True):
        if uq[1] == inf: break
        u_v, u_p = uq # u_v => Value    u_p => Priority

        for adjV in adjDict[u_v]: # for each adj vertex in E in set index u_v
            if u_p + adjV[1] < data.get_p(adjV[0]):
                newP = u_p + adjV[1]
                data.add(adjV[0], newP)

        uq = data.pop() 

    for i in data.status:
        print 'NODE', i, ':', data.status[i][0]
    print 'End Dijkstra', '\n'
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -     

def ShortestPath(data):
    print 'Shortest Reliable Paths Algorithm'
    
    inf = float('inf')
    
    vSet = set()

    for i in data:
        vSet.add(i[0])
        vSet.add(i[1])
    
    loop_s = True
    loop_d = True
    
    source = ''
    k = ''
    tree = []
    
    k = int(raw_input('Integer k : ')[0])
    
    while loop_s:
        if source not in vSet:
            source = raw_input('Source : ')[0]
        else:
            loop_s = False

    
    
    adjDict = {vertex: set() for vertex in vSet} # dic w/ char key and sets of tuples

    for start, end, cost in data:
        adjDict[start].add((end, cost))

    # Didn't get this part  
    print 'NODE ', source, ': 0'
    print 'End Shortest Reliable Paths Algorithm'
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    main()












        


