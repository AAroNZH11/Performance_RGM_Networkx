# Time Performance of Generating Four Types of Random Graphs Using `Networkx`

This repository contains the material for evaluating and reporting the
time performance of generating four important types of random graphs
using the Python package [Networkx](https://networkx.org/). The four 
models are:

1. Erdős-Rényi (ER) [[1]](#1), [[2]](#2) 
2. Watts-Strogatz (WS) [[3]](#3)
3. Barabási-Albert (BA) [[4]](#4), [[5]](#5)
4. Random Geometric Graph (RGG) [[6]](#6)

## Methodology

The time performance for generating each type of random graphs is
measured by the execution time, both at the average and the best,
under a specific setting of the model parameters. We conduct 6 runs
for each parameter setting, discarding the initial (cold) run, and
recording the best/minimal execution time from the subsequent 5
runs. The average of the 5 runs is then calculated.


The parameter common to all four models is the number of
vertices/nodes, denoted as $N$. We vary $N$ from 1000 to 8000 with
step size 1000.  We let the other key parameter(s) for each model vary
as well and use the default values for the remaining parameters.

The experiments are carried out on a Macbook Air M1 with 8GB memory. 

## Result

The execution times for each model are shown below in 2 (3D) plots: one
for the average time (to the left) and the other for the minimal time
(to the right). The execution time measured in seconds is along the z-axis and
varies with the change in model parameter values along the x-axis and y-axis.

![ER](https://github.com/AAroNZH11/Observation_Networkx_RGG/assets/124021215/d5d0c34b-5df6-416b-beff-a27fd8472e01)
![WS](https://github.com/AAroNZH11/Performance_RGM_Networkx/assets/124021215/0281b1ae-e06b-43dd-83d4-adb6dcf76db4)
![BA](https://github.com/AAroNZH11/Performance_RGM_Networkx/assets/124021215/34d3972e-2574-4f6a-9041-b49a68700fbc)
![RGG](https://github.com/AAroNZH11/Performance_RGM_Networkx/assets/124021215/1c8b1d69-f343-48c4-931b-2e202fd96dd7)

## Key Findings

It is observed that the execution time changes almost linearly with
$N$, the number of nodes at a fixed average degree, and changes
non-linearly and smoothly with the average degree as expected, except
for the sudden and sharp increase at the dense graph of N=8000 nodes
with the random geometric graph model.


## Update 

To understand the sudden and sharp increase in generation time for the
large and dense graph with the RGG model, we conducted additional
experiments on another device (windows operating system), with Intel
i7-10875H CPU and 16GB Memory.  Notably, the singular behavior does
not appear on the second device. We conclude that the singular
behavior on the first machine is primarily due to caching operations
within limited memory space.

![Windows_RGG](https://github.com/AAroNZH11/Performance_RGM_Networkx/assets/124021215/abe5dbb6-f0b6-476e-8b74-04e952b1e24e)

## Environment

The experiments were performed on a MacBook Air M1 2021 (8-core CPU
and 8GB Memory) using the Python package `Networkx`.

## Sharing

The empirical finding is shared with the community in the hope of
enhancing our understanding of the performance characteristics of the
`Networkx` package. An intriguing observation made during the project
was the surprising increase in execution time when generating a dense
graph by the Random Geometric Graph (RGG) model. By the additional
experiments on a machine with a larger memory capacity, this
singular behavior is attributed to the caching in limited memory space.



## Acknowledgment

Dr. Nikos Pitsianis, Dr. Dimitris Floros, and Dr. Xiaobai Sun offered
valuable suggestions. My teammate Cody (Chenshuhao) Qin gave me his
advice during the experiments. 

## References

<a id="1">[1]</a>
[Erdős, P., & Rényi, A. (1959). On random graphs. I. Publicationes Mathematicae, 6, 290-297.](https://www.renyi.hu/~p_erdos/1959-11.pdf)

<a id="2">[2]</a>
[Erdős, P., & Rényi, A. (1960). On the evolution of random graphs. Publications of the Mathematical Institute of the Hungarian Academy of Sciences, 5, 17-61.](https://www.renyi.hu/~p_erdos/1960-10.pdf)

<a id="3">[3]</a>
[Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of ‘small-world’ networks. Nature, 393(6684), 440-442.](https://www.nature.com/articles/30918)

<a id="4">[4]</a>
[Barabási, A. L., & Albert, R. (1999). Emergence of scaling in random networks. Science, 286(5439), 509-512.](https://www.science.org/doi/10.1126/science.286.5439.509)

<a id="5">[5]</a>
[Barabási, A. L., & Albert, R. (2011). Scale-Free Networks: A Decade and Beyond. Science, 325(5939), 412-413.](https://www.science.org/doi/10.1126/science.1173299)

<a id="6">[6]</a>
[Penrose, M. D. (2003). Random geometric graphs. Oxford University Press.](https://academic.oup.com/book/9064)

<a id="7">[7]</a>
[Exploring network structure, dynamics, and function using NetworkX](https://conference.scipy.org/proceedings/SciPy2008/paper_2/)

<a id="8">[8]</a>
[ J. D. Hunter, "Matplotlib: A 2D Graphics Environment", Computing in Science & Engineering, vol. 9, no. 3, pp. 90-95, 2007.](https://ieeexplore.ieee.org/document/4160265)

<a id="9">[9]</a>
[Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). DOI: 10.1038/s41586-020-2649-2](https://www.nature.com/articles/s41586-020-2649-2)

