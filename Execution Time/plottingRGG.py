import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv('times_RGG.csv')

# The 'Nodes' column is your first parameter
param1 = df['Nodes'].values

# The other columns are your second parameter and corresponding execution times
param2 = df.columns[1:].astype(float)  # Convert to float for plotting

# Convert DataFrame into a 2D array for plotting
execution_times = df.iloc[:, 1:].values

# Create a figure
fig = plt.figure()

# Create a 3D axis
ax = fig.add_subplot(111, projection='3d')

# The width of the bars
dx = dy = 0.8
dz = execution_times.flatten()

# The starting point of the bars
_x = np.repeat(np.arange(len(param1)), len(param2))
_y = np.tile(np.arange(len(param2)), len(param1))
_z = np.zeros_like(dz)

# The bars positions on x, y and z axes
x = [i + 0.5 for i in _x]
y = [i + 0.5 for i in _y]
z = _z

# Plot the bars
ax.bar3d(x, y, z, dx, dy, dz, color=(0.6, 0.8, 1.0), shade=True)

# Set labels
ax.set_xlabel('Number of nodes')
ax.set_xticks([i + 0.5 for i in range(len(param1))])
ax.set_xticklabels(param1)

ax.set_ylabel('Radius')
ax.set_yticks([i + 0.5 for i in range(len(param2))])
ax.set_yticklabels(param2)

ax.set_zlabel('Execution time (s)')

# Add a title
ax.set_title('Execution Time of RGG model')

# Add some text
text_x = len(param1) / 2
text_y = len(param2) / 2
text_z = np.max(dz) + 5  # Adjust the position of the text along the z-axis
ax.text(text_x, text_y, text_z, 'Graph Generator: Networkx\nMachine: Macbook Air M1 2021', color='red', fontsize=12)

# Show the plot
plt.show()
