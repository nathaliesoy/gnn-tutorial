import torch
import torch.nn as nn
import dgl 
import dgl.function as fn

class JetNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.init_net = InitNet()

        self.mpnn = MPNN()

        self.final_net = FinNet()

    def forward(self, g):

        # pass the graph through the initial network, the message passing network and the final network
        return g


class InitNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.particle_mlp = 

        self.jet_mlp = 

    def forward(self, g):
        
        # concatenate all particle features into a single tensor
        # use the particle_mlp to get a hidden representation 'h' for each particle
        # do the same for the jet features to create a global representation 'jet_feat' for the jet
        # broadcast the global jet representation as an additional feature to all particles
        
        return g



class MPNN(nn.Module):
    def __init__(self):
        super().__init__()

        # define the number of message passing blocks, you can start with 1 in the beginning
        self.n_iter = 1

        self.node_update_networks = nn.ModuleList()
        for iter_i in range(self.n_iter):    
            self.node_update_networks.append(NodeNet())
        

    def forward(self, g):
        # first get the global hidden representation
        # then loop over the number of message passing blocks
        # in each iteration first update edges and nodes and then update the global hidden representation
        return g
    
    def update_global(self, g):
        # sum all particle hidden representations and normalize
        # update the global rep with the new global rep
        # broadcast the global rep to all particles



class NodeNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.node_network = ...

    def forward(self, nodes):
        # get the messages from the edges and sum them up
        # combine all relevant information that you need and pass it throught the node network
        # normalize your outputs 
        return 
    
class FinNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.final_mlp = ...

    def forward(self, g):
        # pass global hidden rep through the final mlp to get the 
        return g
