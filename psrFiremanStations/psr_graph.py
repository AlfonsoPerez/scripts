from constraint import *
import sys

# Variables
variables = ("a","b","c","d","e")

# Adjacency matrix for star S4
#adj_mat = [[1,0,0,0,1],[0,1,0,0,1],[0,0,1,0,1],[0,0,0,1,1],[1,1,1,1,1]]

# Adjacency matrix for path P4
adj_mat = [[1,1,0,0,0],[1,1,1,0,0],[0,1,1,1,0],[0,0,1,1,1],[0,0,0,1,1]]

def union_sets(list_nodes):
    chains = list()
    for i,k in enumerate(list_nodes):
        if k:
            for j,n in enumerate(adj_mat[i]):
                if n:
                    chains.append(j)
    return set(chains)

problem = Problem(BacktrackingSolver())
problem.addVariables(variables,[0,1])


problem.addConstraint(lambda a, b, c, d, e: list(union_sets([a,b,c,d,e])) == [0,1,2,3,4],variables)

length_solution = sys.maxint
min_sol = None

for solution in problem.getSolutionIter():

    sum_nodes = 0
    for node in solution:
        sum_nodes += solution[node]

    if sum_nodes <= length_solution:
        min_sol = solution
        length_solution = sum_nodes

print (min_sol)


