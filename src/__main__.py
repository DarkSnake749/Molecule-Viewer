from molecule_builder import *
from direct.showbase.ShowBase import ShowBase

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Disable the camera trackball controls.
        #self.disableMouse()

        mol = Molecule(self.render, "FC(CC(C(C1(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(CC2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)C2Cl)I)Cl)C1Br")
        mol.build_molecule()
        self.render.ls()

def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
