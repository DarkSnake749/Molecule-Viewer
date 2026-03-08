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
            "[Ag+].[N+](=O)([O-])[O-]",
        )
        mol.build_molecule()
        mol.set_pos(0, 20, 0)

        self.custom_cam = Camera(self)

        taskMgr.add(self.custom_cam.update, "camera-update")

        #self.render.ls()

def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
