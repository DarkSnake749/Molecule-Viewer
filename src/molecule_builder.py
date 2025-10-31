from utils import *

class Molecule:
    def __init__(self, render, smiles):
        self.render = render
        self.data = smiles_to_3d_data(smiles)

        self.reset_atoms = []
        self.reset_bonds = []

        self.atoms = []
        self.bonds = []
    
    def build_molecule(self):

        # Create atoms
        for atom in self.data["atoms"]:
            new_atom = make_sphere(self.render, atom['radius'], atom['color'])
            new_atom.set_pos((atom['x'],atom['y'],atom['z']))
            self.reset_atoms.append(new_atom)
        
        # Create bonds
        for bond in self.data["bonds"]:
            start_atom = self.data["atoms"][bond["start"]]
            end_atom = self.data["atoms"][bond["end"]]
            new_bond = make_cylinder (
                self.render,
                start=(start_atom['x'], start_atom['y'], start_atom['z']),
                end=(end_atom['x'], end_atom['y'], end_atom['z']), 
                radius=(0.1 * bond['order']),
                color=(1, 1, 1, 1),
            )
            self.reset_bonds.append(new_bond)
        
        self.reset()
    
    def reset(self):
        self.atoms = self.reset_atoms
        self.bonds = self.reset_bonds

    def move(self): ...
    def rotate(self): ...
    def scale(self): ...
    def update(self): ...


    