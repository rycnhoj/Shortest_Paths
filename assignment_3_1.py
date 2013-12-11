##import Queue
import itertools
from heapq import heapify, heappush, heappop

class PriorityQueue():
    def __init__(self):
        self.pq = []
        self.status = {}
        self.REMOVED = '<removed-task>'

    def add_task(self, task, priority=0):
        entry = [priority, task]
        self.status[task] = entry
        heappush(self.pq, entry)

    def pop_task(self):
        priority, task = heappop(self.pq)
        return (task, priority)

    def empty(self):
        return len(self.pq) == 0
            
    def printPQ(self):
        for x in self.pq:
            print x[1], ':', x[0], ''

    def get_p(self, value):
        if value in self.status:
            return self.status[value][0]

def main():
    fileName = raw_input('Enter Filename: ')
    readFile = open(fileName)

    setMode = True
    
    G = []

    directed = ''
    
    for line in readFile:
        if line[0] != '#':
            if setMode:
                if line[0] == 'D':
                    print 'Directed'
                    directed = True
                elif line[0] == 'UD':
                    print 'Undirected'
                    directed = False
                setMode = False
            else:
                if directed:
                    temp = line.split()
                    G.append((temp[0], temp[1], int(temp[2])))
                else:
                    temp = line.split()
                    G.append((temp[0], temp[1], int(temp[2])))
                    G.append((temp[1], temp[0], int(temp[2])))
    
    Dijkstra(G, directed)

def Dijkstra(G, directed):

    inf = float('inf')
    
    vSet = set()

    for i in G:
        vSet.add(i[0])
        vSet.add(i[1])
    
    loop = True
    source = ''
    
    while loop:
        if source not in vSet:
            source = raw_input('SOURCE: ')[0]
        else:
            loop = False

    s = 'A'
    adjDict = {vertex: set() for vertex in vSet} # dic w/ char key and sets of tuples

    for start, end, cost in G:
        adjDict[start].add((end, cost))

    Q = PriorityQueue()

    for i in vSet:
        if i == s:
            Q.add_task(i, 0)
        else:
            Q.add_task(i, inf)

    uq = Q.pop_task() # Pop min Starting node
        
    while(True):
        if uq[1] == inf: break
        u_v, u_p = uq # u_v => Value    u_p => Priority

        for adjV in adjDict[u_v]: # for each adj vertex in E in set index u_v
            if u_p + adjV[1] < Q.get_p(adjV[0]):
                newP = u_p + adjV[1]
                Q.add_task(adjV[0], newP)

        uq = Q.pop_task() 

    for i in Q.status:
        print 'NODE', i, ':', Q.status[i][0]
    print 'End Dijkstra'

if __name__ == '__main__':
    main()












        


