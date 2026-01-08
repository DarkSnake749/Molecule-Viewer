from direct.showbase.ShowBase import ShowBase

from camera import *
from molecule import *
from text import *

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Disable the camera trackball controls.
        self.disableMouse()

        mol = Molecule(
            self.render, 
            "CCO",
            "molecule1"
        )

        mol.set_pos(0, 20, 0)
        mol.build_molecule()

        mol2 = Molecule(
            self.render, 
            "CCO",
            "molecule2"
        )

        mol2.set_pos(5, 20, 0)
        mol2.build_molecule()

        test_text = Text3D(self.render, "test-text", "Hello, World!", self.loader)
        test_text.set_scale(1)
        test_text.set_position(0, 30, 5)

        self.custom_cam = Camera(self)

        taskMgr.add(self.custom_cam.update, "camera-update")

        # self.render.ls()

def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
