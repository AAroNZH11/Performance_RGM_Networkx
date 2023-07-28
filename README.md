# Graph Generation Time Analysis with Networkx

This repository contains an analysis of the execution time required for generating graphs using various models in the [Networkx](https://networkx.org/) Python package. The models evaluated include:

1. Erdős-Rényi (ER)
2. Watts-Strogatz (WS)
3. Barabási-Albert (BA)
4. Random Geometric Graph (RGG)

## Methodology

The execution time for generating graphs is measured for different numbers of nodes (ranging from 1000 to 8000) and various parameters specific to each model. Each configuration is run 6 times (results of first cold run were thrown out) to get a reliable estimate of the execution time.

## Key Findings

It is observed that the time taken to generate a graph using the Random Geometric Graph model can be abnormally long under certain conditions. Specifically, when the number of nodes is large (up to 8000 nodes) and the radius is relatively high (0.8), the execution time is more than five times the estimated time.

## Data and Visualizations

The data for this analysis is included in the repository in CSV format. Additionally, for each graph generation model, execution time plots with various parameters have been created and included in this repository.

## Environment

The analysis was performed on a MacBook Air M1 2021 (8-core CPU and 8GB Memory) using Python and the Networkx package.

## Sharing

This finding is shared with the community in the hope of enhancing our understanding of the performance characteristics of the Networkx package. An intriguing observation made during the project was the surprising increase in execution time when generating a graph using the Random Geometric Graph model. Specifically, the execution time increases markedly when the graph reaches around 8000 nodes and the radius is set at 0.8.

Understanding the cause of this performance drop is part of the motivation behind sharing this research. If you have insights, theories, or even a solution for this issue, it could greatly enhance the efficiency and usability of Networkx for complex, large-scale graph generation and analysis.

Contributions, insights, or suggestions are warmly welcomed. Please feel free to create an issue or a pull request if you have any thoughts on this topic or other aspects of the project.

## Acknowledgement

Thanks for Dr. Nikos Pitsianis, Dr. Dimitris Floros and Dr. Xiaobai Sun for their valuable comments.
