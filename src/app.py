from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight

from camera import *
from molecule import *
from text import *

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Disable the camera trackball controls.
        self.disableMouse()

        """
        Test element

        mol = Molecule(
            self.render,
            "[Ag+].[N+](=O)([O-])[O-]",
        )
        mol.build_molecule()
        mol.set_pos(0, 20, 0)

        text = Text3D(self.render, "Hi", "Hello, World", self.loader)
        text.set_position(0, 20, 5)
        
        """

        # * Reaction #1
        self.water1 = Molecule(self.render, "[H]O[H]")
        self.water2 = Molecule(self.render, "[H]O[H]")
        self.oxygen = Molecule(self.render, "O=O")
        self.hydrogen = Molecule(self.render, "[H][H]")

        self.setup_reaction_1()

        self.all_molecule = [
            self.water1, self.water2, self.oxygen, self.hydrogen,

        ]
        self.rotation_speed = 0.15
        self.custom_cam = Camera(self)
        self.setup_lighting()
        self.setBackgroundColor(0.8745, 0.9216, 0.9176)
        self.render.setShaderAuto()

        taskMgr.add(self.custom_cam.update, "camera-update")
        taskMgr.add(self.update_shader, "shader-update")

        taskMgr.add(self.update_rotation, "rotation-update")

        #self.render.ls()
    
    def update_shader(self, task):
        self.render.setShaderInput("camera_pos", self.camera.getPos(self.render))
        return task.cont
    
    def setup_lighting(self):

        # Ambient light
        ambient = AmbientLight("ambient")
        ambient.setColor((0.25, 0.25, 0.3, 1))
        ambient_np = self.render.attachNewNode(ambient)
        self.render.setLight(ambient_np)

        # Key light
        key = DirectionalLight("key")
        key.setColor((1, 1, 0.95, 1))
        key_np = self.render.attachNewNode(key)
        key_np.setHpr(45, -60, 0)
        self.render.setLight(key_np)

        # Fill light
        fill = DirectionalLight("fill")
        fill.setColor((0.5, 0.6, 1.0, 1))
        fill_np = self.render.attachNewNode(fill)
        fill_np.setHpr(-45, -20, 0)
        self.render.setLight(fill_np)

    def setup_reaction_1(self):
        self.water1.build_molecule()
        self.water1.set_pos(0, 20, 0)

        self.water2.build_molecule()
        self.water2.set_pos(0, 20, 2)

        to = Text3D(self.render, "React1_to", ">", self.loader)
        to.set_position(2.5, 20, 0.5)

        self.oxygen.build_molecule()
        self.oxygen.set_pos(5, 20, 0.75)

        plus = Text3D(self.render, "React1_plus", "+", self.loader)
        plus.set_position(7.5, 20, 0.5)

        self.hydrogen.build_molecule()
        self.hydrogen.set_pos(10, 20, 0.75)

    def setupt_reaction_2(self):
        pass
    
    def update_rotation(self, task):
        for i, mol in enumerate(self.all_molecule):
            h, p, r = mol.get_rot()
            self.all_molecule[i].set_rotation(h+self.rotation_speed, p+self.rotation_speed, r+self.rotation_speed)
        return task.cont

def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
