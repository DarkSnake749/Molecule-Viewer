from panda3d.core import Vec3
import math
import itertools

from utils import *

# TODO: Show the molecule
# TODO: change the reset list name
# TODO: Debug

# TODO: Move, rotate, scale function
# TODO: Keyboard input
# TODO: UI (win size, input box)

class Molecule:
    def __init__(self, render, smiles):
        self.render = render
        self.atoms, self.bonds = smiles_to_3d_molecule(smiles)
        self.root = NodePath("molecule")
        self.root.reparent_to(render)
    
    def draw_bond(self, start, end, order, radius, color):
        direction = (end - start)
        direction.normalize()

        perp = direction.cross(Vec3(0, 0, 1))
        if perp.length() < 0.01:
            perp = direction.cross(Vec3(0, 1, 0))
        perp.normalize()

        spacing = radius * 2.5

        offsets = {
            1: [0],
            2: [-spacing / 2, spacing / 2],
            3: [-spacing, 0, spacing]
        }[order]

        for offset in offsets:
            shift = perp * offset
            make_cylinder(
                self.render,
                start=start + shift,
                end=end + shift,
                radius=radius,
                color=color
            )

    def build_molecule(
        self,
        atom_radii=None,
        atom_colors=None,
        bond_radius=0.08,
        bond_color=(0.6, 0.6, 0.6, 1)
    ):
        """
        Build molecule using real RDKit bonds and per-element atom radii.
        """

        vec_atoms = [Vec3(*a["pos"]) for a in self.atoms]

        # ---- Draw atoms ----
        for atom, pos in zip(self.atoms, vec_atoms):
            element = atom["element"]
            radius = covalent_to_visual_radius(element, COVALENT_RADII, scale=0.5) #COVALENT_RADII.get(element, 0.3)
            color = CPK_COLORS.get(element, (0.7, 0.7, 0.7, 1))

            sphere = make_sphere(
                self.render,
                radius=radius,
                color=color
            )
            sphere.set_pos(pos)

        # ---- Draw bonds ----
        for bond in self.bonds:
            self.draw_bond(
                vec_atoms[bond["a"]],
                vec_atoms[bond["b"]],
                order=bond["order"],
                radius=bond_radius,
                color=bond_color
            )
        