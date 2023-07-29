import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df_avg = pd.read_csv('times_RGG.csv')
df_best = pd.read_csv('best_time_RGG.csv')

# The 'Nodes' column is your first parameter
param1 = df_avg['Nodes'].values

# The other columns are your second parameter and corresponding execution times
param2 = df_avg.columns[1:].astype(float)  # Convert to float for plotting

# Convert DataFrame into a 2D array for plotting
execution_times_avg = df_avg.iloc[:, 1:].values
execution_times_best = df_best.iloc[:, 1:].values

# Create a figure
fig = plt.figure(figsize=(16, 8))

# Create a 3D axis for average times
ax1 = fig.add_subplot(121, projection='3d')

# Plot the bars for average times
_x = np.repeat(np.arange(len(param1)), len(param2))
_y = np.tile(np.arange(len(param2)), len(param1))
_z = np.zeros_like(execution_times_avg.flatten())

x, y, z = [i + 0.5 for i in _x], [i + 0.5 for i in _y], _z
dx = dy = 0.6  # Smaller bars
dz = execution_times_avg.flatten()  # Heights of the bars

ax1.bar3d(x, y, z, dx, dy, dz, color=(0.6, 0.8, 1.0), shade=True)

# Set labels and title for the average times plot
ax1.set_xlabel('Number of nodes')
ax1.set_xticks([i + 0.5 for i in range(len(param1))])
ax1.set_xticklabels(param1)

ax1.set_ylabel('Radius')
ax1.set_yticks([i + 0.5 for i in range(len(param2))])
ax1.set_yticklabels(param2)

ax1.set_zlabel('Average Execution time (s)')
ax1.set_title('Average Execution Time of RGG model')

# Create a 3D axis for best times
ax2 = fig.add_subplot(122, projection='3d')

# Plot the bars for best times
_z = np.zeros_like(execution_times_best.flatten())
dz = execution_times_best.flatten()  # Heights of the bars

ax2.bar3d(x, y, z, dx, dy, dz, color=(0.6, 0.8, 1.0), shade=True)

# Set labels and title for the best times plot
ax2.set_xlabel('Number of nodes')
ax2.set_xticks([i + 0.5 for i in range(len(param1))])
ax2.set_xticklabels(param1)

ax2.set_ylabel('Radius')
ax2.set_yticks([i + 0.5 for i in range(len(param2))])
ax2.set_yticklabels(param2)

ax2.set_zlabel('Best Execution time (s)')
ax2.set_title('Best Execution Time of RGG model')

# Add some text
text_x = len(param1) / 2
text_y = len(param2) / 2
text_z = max(np.max(execution_times_avg), np.max(execution_times_best)) + 5
fig.text(0.5, 0.02, 'Graph Generator: Networkx\nMachine: Macbook Air M1 \n 8GB Memory', ha='center', color='red', fontsize=12)

z_ticks = np.arange(0,275,25)
# Set z-ticks for average times plot
ax1.set_zticks(z_ticks)
# Set z-ticks for best times plot
ax2.set_zticks(z_ticks)

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
