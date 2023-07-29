import timeit
import networkx as nx
import pandas as pd

nodes = [1000,2000,3000,4000,5000,6000,7000,8000]  # Number of nodes
radius_values = [0.2,0.3,0.4,0.5]  # Radius

runs = 6  # Number of times to run the code for each (n, r) pair

def your_code(n, r):
    G = nx.random_geometric_graph(n, r)
    # Other code if necessary
    pass

data_avg = {'Nodes': nodes}
data_best = {'Nodes': nodes}

for r in radius_values:
    avg_times = []
    best_times = []
    for n in nodes:
        run_times = []
        for run in range(runs):
            start_time = timeit.default_timer()
            your_code(n, r)
            execution_time = timeit.default_timer() - start_time
            run_times.append(execution_time)
        avg_time = sum(run_times[1:]) / (runs - 1)  # Average time, ignoring the first run
        best_time = min(run_times[1:])  # Best time, ignoring the first run
        avg_times.append(avg_time)
        best_times.append(best_time)
    data_avg[str(r)] = avg_times
    data_best[str(r)] = best_times

df_avg = pd.DataFrame(data_avg)
df_avg.to_csv('times_RGG.csv', index=False)

df_best = pd.DataFrame(data_best)
df_best.to_csv('best_time_RGG.csv', index=False)
