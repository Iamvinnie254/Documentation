import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall

arr = np.array([[1,2,3],[4,5,6],[0,1,0]])
newarr = csr_matrix(arr)

print(connected_components(newarr))


##Dijkstra method for finding the shortest path in a graph from one element to another

print(dijkstra(newarr, return_predecessors=True, indices= 0))

##Floyd warshall method for finding also shortes path between all pairs of elements

print(floyd_warshall(newarr, return_predecessors=True))