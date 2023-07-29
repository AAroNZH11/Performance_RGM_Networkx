# Time Performance of generaing graphs by 4 Models using Python package Networkx

This repository contains collecting and observing the execution time required for generating graphs using various models in the [Networkx](https://networkx.org/) Python package. The models evaluated include:

1. Erdős-Rényi (ER) (["On Random Graphs. I"](https://www.renyi.hu/~p_erdos/1959-11.pdf), ["On the evolution of random graphs"](https://www.renyi.hu/~p_erdos/1960-10.pdf))
2. Watts-Strogatz (WS) (["Collective dynamics of ‘small-world’ networks"](https://www.nature.com/articles/30918))
3. Barabási-Albert (BA) (["Emergence of Scaling in Random Networks"](https://www.science.org/doi/10.1126/science.286.5439.509), ["Scale-Free Networks: A Decade and Beyond"](https://www.science.org/doi/10.1126/science.1173299))
4. Random Geometric Graph (RGG) (["Random Geometric Graphs"](https://academic.oup.com/book/9064))

## Methodology

In the process of generating graphs, the execution time is meticulously tracked for diverse numbers of nodes, ranging from 1000 to 8000, and various parameters unique to each model. To ensure accurate assessments, every configuration undergoes 6 runs, with the initial cold run results discarded. Both the average time of the last five runs and the best run (minimum time) are recorded for analysis and comparison.

## Result
Results of the execution times for each models are shown below in 3D plots
![ER](https://github.com/AAroNZH11/Observation_Networkx_RGG/assets/124021215/d5d0c34b-5df6-416b-beff-a27fd8472e01)
![WS](https://github.com/AAroNZH11/Observation_Networkx_RGG/assets/124021215/573d9dba-5fbb-4a91-8d2f-cc01b8383d78)
![BA](https://github.com/AAroNZH11/Observation_Networkx_RGG/assets/124021215/9dd54182-1f49-4d61-8e2a-c19defb1feff)
![RGG](https://github.com/AAroNZH11/Observation_Networkx_RGG/assets/124021215/e5a196c5-b7b2-4b5d-bfc3-e8d4bd75cd1c)

## Key Findings

It is observed that the time taken to generate a graph using the Random Geometric Graph model can be abnormally long under certain conditions. Specifically, when the number of nodes is large (up to 8000 nodes) and the radius is relatively high (up to 0.8).

## Update 
Tests are made on another device (windows operating system), with Intel i7-10875H CPU and 16GB Memory, execution time of Random Geometric Graph became normal. The reason for obtaining different results in two different configurations could be attributed to differences in memory availability.
![windows_RGG](https://github.com/AAroNZH11/Performance_RGM_Networkx/assets/124021215/7c5cefc4-0c31-4b6a-bfda-f1c5088b0afe)

## Environment

The analysis was performed on a MacBook Air M1 2021 (8-core CPU and 8GB Memory) using Python package Networkx.

## Sharing

This finding is shared with the community in the hope of enhancing our understanding of the performance characteristics of the Networkx package. An intriguing observation made during the project was the surprising increase in execution time when generating a graph using the Random Geometric Graph model. Specifically, the execution time increases markedly when the graph reaches around 8000 nodes and the radius is set at 0.8.

If you have insights, theories, or even a solution for this issue, it could greatly enhance the efficiency and usability of Networkx for complex, large-scale graph generation and analysis. Please feel free to create an issue or a pull request if you have any thoughts on this topic or other aspects of the project.

## Acknowledgement

Thanks for Dr. Nikos Pitsianis, Dr. Dimitris Floros and Dr. Xiaobai Sun for their valuable comments, and thanks Chenshuhao Qin for his advice.

## Citations

[Erdős, P., & Rényi, A. (1959). On random graphs. I. Publicationes Mathematicae, 6, 290-297.](https://www.renyi.hu/~p_erdos/1959-11.pdf)

[Erdős, P., & Rényi, A. (1960). On the evolution of random graphs. Publicationes of the Mathematical Institute of the Hungarian Academy of Sciences, 5, 17-61.](https://www.renyi.hu/~p_erdos/1960-10.pdf)

[Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of ‘small-world’ networks. Nature, 393(6684), 440-442.](https://www.nature.com/articles/30918)

[Barabási, A. L., & Albert, R. (1999). Emergence of scaling in random networks. Science, 286(5439), 509-512.](https://www.science.org/doi/10.1126/science.286.5439.509)

[Barabási, A. L., & Albert, R. (2011). Scale-Free Networks: A Decade and Beyond. Science, 325(5939), 412-413.](https://www.science.org/doi/10.1126/science.1173299)

[Penrose, M. D. (2003). Random geometric graphs. Oxford University Press.](https://academic.oup.com/book/9064)

[Exploring network structure, dynamics, and function using NetworkX](https://conference.scipy.org/proceedings/SciPy2008/paper_2/)

[ J. D. Hunter, "Matplotlib: A 2D Graphics Environment", Computing in Science & Engineering, vol. 9, no. 3, pp. 90-95, 2007.](https://ieeexplore.ieee.org/document/4160265)

[Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). DOI: 10.1038/s41586-020-2649-2](https://www.nature.com/articles/s41586-020-2649-2)

