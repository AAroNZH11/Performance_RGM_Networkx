import timeit
import networkx as nx
import pandas as pd

nodes = [1000,2000,3000,4000,5000,6000,7000,8000]
p = [0.2,0.4,0.6,0.8]
runs = 6  # Number of times to run the code for each (n, p) pair

def your_code(n, r):
    G = nx.erdos_renyi_graph(n, r)
    # Other code if necessary
    pass

data = {'Nodes': nodes}
for prob in p:
    times = []
    for n in nodes:
        total_time = 0
        for run in range(runs):
            start_time = timeit.default_timer()
            your_code(n, prob)
            execution_time = timeit.default_timer() - start_time
            # Ignore the time from the first run
            if run != 0:
                total_time += execution_time
        average_time = total_time / (runs - 1)
        times.append(average_time)
    data[str(prob)] = times

df = pd.DataFrame(data)
df.to_csv('times_ER.csv', index=False)
