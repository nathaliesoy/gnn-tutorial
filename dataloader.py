import h5py

import torch
from torch.utils.data import Dataset

import dgl

class JetDataset(Dataset):
    def __init__(self, filename, n_events = 700_000):

        self.nevents = n_events

        # load file
        # load jet and particle features from file
        
        self.get_scale_dict() # see below
        # scale jet features
        
        # close file

        print('done loading data')



    def get_single_item(self, idx):

        n_part = # get number of particles in this jet

        # define edges
        # particle to particle edges, connect every particle to every other particle (including itself)
        # create also a global node for the jet features
        

        # create graph

        # fill the node features:
        # put the particle features pt, eta, phi on the 'particles' node type
        # put the jet feature pt, mass, eta, class on the 'global_node' node type
        # note that the class is the target and will later be used only for loss calculation

        return g

        
    def __len__(self):
        return self.nevents 

    def __getitem__(self, idx):
        return self.get_single_item(idx)
    
        
    def get_scale_dict(self):  
        # put here the mean and std of the jet features as calculated in the notebook
        self.scale_dict = {
            'jet_pt' : {'mean' : 0, 'std' : 1},
            'jet_eta' : {'mean' : 0, 'std' : 1},
            'jet_mass' : {'mean' : 0, 'std' : 1}}


# this function is provided for you, it is used to batch multiple graphs together
# dgl creates one big graph with all the nodes and edges from the batch 
# and keeps track of which nodes and edges belong to which graph
def collate_graphs(samples):
    batched_graphs = dgl.batch(samples)
    return batched_graphs