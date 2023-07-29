import timeit
import networkx as nx
import pandas as pd

nodes = [1000,2000,3000,4000,5000,6000,7000,8000] # number of nodes
k = [50,100,150,200] # each node is connected to ’k’ nearest neighbors in a ring topology
p = 0.01 # rewiring probability

runs = 6  # Number of times to run the code for each (n, k, p) pair

def your_code(n, k, p):
    G = nx.watts_strogatz_graph(n, k, p)
    # Other code if necessary
    pass

data_avg = {'Nodes': nodes}
data_best = {'Nodes': nodes}

for neighbors in k:
    avg_times = []
    best_times = []
    for n in nodes:
        run_times = []
        for run in range(runs):
            start_time = timeit.default_timer()
            your_code(n, neighbors, p)
            execution_time = timeit.default_timer() - start_time
            run_times.append(execution_time)
        avg_time = sum(run_times[1:]) / (runs - 1)  # Average time, ignoring the first run
        best_time = min(run_times[1:])  # Best time, ignoring the first run
        avg_times.append(avg_time)
        best_times.append(best_time)
    data_avg[str(neighbors)] = avg_times
    data_best[str(neighbors)] = best_times

df_avg = pd.DataFrame(data_avg)
df_avg.to_csv('times_WS.csv', index=False)

df_best = pd.DataFrame(data_best)
df_best.to_csv('best_time_WS.csv', index=False)
