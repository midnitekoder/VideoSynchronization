import numpy
import csv
from collections import defaultdict
from operator import itemgetter
from createVideo import createVideos
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    self.distances[(to_node), from_node] = distance

def getPath(path, node, lis):
  lis.append(node)
  if(node == 1):
    return lis
  return getPath(path, path[node], lis)

def coord(node, rows, cols):
  col = node % cols
  if col == 0:
    col = cols
  return ((node - 1) / cols + 1, col)

def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path
# @vincentarelbundock

# graph = Graph();
# graph.add_node(1);
# graph.add_node(2);
# graph.add_node(3);
# graph.add_node(4);
# graph.add_node(5);
# graph.add_node(6);
# graph.add_edge(1,2,5);
# graph.add_edge(1,4,9);
# graph.add_edge(1,6,2);
# graph.add_edge(2,3,2);
# graph.add_edge(3,4,3);
# graph.add_edge(4,5,2);
# graph.add_edge(5,6,3);



reader=csv.reader(open("finalMatrix.txt","rb"),delimiter=',')
x=list(reader)
result=numpy.array(x).astype('float')

rows = len(result)
cols = len(result[42])

print rows, cols

i=1
graph = Graph()

while i <= rows*cols:
  graph.add_node(i)
  i += 1

r = 0
c = 1

while r < rows:
  c = 1
  while c < cols:
    graph.add_edge(r * cols + c, r * cols + c + 1, result[r][c])
    c += 1
  r += 1

r = 0
c = 1

while c <= cols:
  r = 0
  while r < rows - 1:
    graph.add_edge(c + cols * r, c + cols * ( r + 1 ), result[r+1][c-1])
    r += 1
  c += 1

r = 0
c = 1

while c < cols:
  r = 0
  while r < rows - 1:
    graph.add_edge(c + cols * r, ( c + 1 ) + cols * ( r + 1 ), result[r+1][c])
    r += 1
  c += 1

visited, path = dijsktra(graph, 1)
vis = {}

c = cols - 1
r = 0

while r < rows:
  vis[(r + 1) * cols] = visited[(r + 1) * cols - 1]
  r += 1

cell = min(vis.iteritems(), key=itemgetter(1))

lis = []

nodesList = getPath(path,18810,lis)

print nodesList
coordinateList=[]
for each in nodesList:
  row,column= coord(each, rows, cols)
  dicPathcoord={}
  dicPathcoord['frame1']=row
  dicPathcoord['frame2']=column
  coordinateList.append(dicPathcoord)
newlist = sorted(coordinateList, key=lambda k: k['frame1'])
createVideos(newlist,rows,cols)

