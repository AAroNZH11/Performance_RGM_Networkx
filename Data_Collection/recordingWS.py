import timeit
import networkx as nx
import pandas as pd

nodes = [1000,2000,3000,4000,5000,6000,7000,8000] # number of nodes
k = [50,100,150,200] # each node is connected to ’k’ nearest neighbors in a ring topology
p = 0.01 # rewiring probability

runs = 6  # Number of times to run the code for each (n,k,p) pair

def your_code(n, k, p):
    G = nx.watts_strogatz_graph(n, k, p)
    # Other code if necessary
    pass

data = {'Nodes': nodes}
for neighbors in k:
    times = []
    for n in nodes:
        total_time = 0
        for run in range(runs):
            start_time = timeit.default_timer()
            your_code(n, neighbors, p)
            execution_time = timeit.default_timer() - start_time
            # Ignore the time from the first run
            if run != 0:
                total_time += execution_time
        average_time = total_time / (runs - 1)
        times.append(average_time)
    data[str(neighbors)] = times

df = pd.DataFrame(data)
df.to_csv('times_WS.csv', index=False)
