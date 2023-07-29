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

data_avg = {'Nodes': nodes}
data_best = {'Nodes': nodes}

for edges in m:
    avg_times = []
    best_times = []
    for n in nodes:
        run_times = []
        for run in range(runs):
            start_time = timeit.default_timer()
            your_code(n, edges)
            execution_time = timeit.default_timer() - start_time
            run_times.append(execution_time)
        avg_time = sum(run_times[1:]) / (runs - 1)  # Average time, ignoring the first run
        best_time = min(run_times[1:])  # Best time, ignoring the first run
        avg_times.append(avg_time)
        best_times.append(best_time)
    data_avg[str(edges)] = avg_times
    data_best[str(edges)] = best_times

df_avg = pd.DataFrame(data_avg)
df_avg.to_csv('times_BA.csv', index=False)

df_best = pd.DataFrame(data_best)
df_best.to_csv('best_time_BA.csv', index=False)
