import timeit
import networkx as nx
import pandas as pd

nodes = [1000,2000,3000,4000,5000,6000,7000,8000]  # Number of nodes
m = [1,2,3,4]  # Number of edges to attach from a new node to existing nodes

runs = 6  # Number of times to run the code for each (n, m) pair

def your_code(n, m):
    G = nx.barabasi_albert_graph(n, m)
    # Other code if necessary
    pass

data = {'Nodes': nodes}
for edges in m:
    times = []
    for n in nodes:
        total_time = 0
        for run in range(runs):
            start_time = timeit.default_timer()
            your_code(n, edges)
            execution_time = timeit.default_timer() - start_time
            # Ignore the time from the first run
            if run != 0:
                total_time += execution_time
        average_time = total_time / (runs - 1)
        times.append(average_time)
    data[str(edges)] = times

df = pd.DataFrame(data)
df.to_csv('times_BA.csv', index=False)
