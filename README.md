# ex-gnn
Tutorial on Graph Neural Networks for Particle Jet Classification using Deep Graph Library

Graph Neural Networks (GNNs) were developed to handle data structures where the data points lack an explicit order but have interconnected relationships. Examples of such structures include molecules or social networks, both of which can be effectively represented as graphs. In recent years, GNNs have also gained popularity in particle physics for various applications.

One example where a graph representation proved beneficial in particle physics is the representation of “jets”. Jets are concentrated sprays of particles resulting from the decay of an unstable particle generated in a highly energetic particle collision. A single collision typically produces multiple jets (see image below), each containing information about its originating particle. Extracting this information helps us understand what fundamental particles were created in the collision, which is crucial for many particle physics analyses.

<img width="491" alt="Screenshot 2024-02-26 at 17 13 28" src="https://github.com/ai-hub-weizmann/ex-gnn/assets/73601976/e0f30fd7-0384-4af9-b886-5512bfd22b91">

In this tutorial, we will develop a GNN for jet classification. Given the properties of the jet constituents, the task is to build a network that will predict the particle type that created the jet. First, we will learn about the data and the different types of jets and particles to get an intuitive understanding of the task. Further, we will get familiar with DGL (Deep Graph Library), a very useful package for GNNs, and work through all the building blocks needed to build the network.
