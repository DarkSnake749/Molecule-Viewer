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
        self.water1 = Molecule(self.render, "O")
        self.water2 = Molecule(self.render, "O")
        self.oxygen = Molecule(self.render, "O=O")
        self.hydrogen = Molecule(self.render, "[H][H]")

        # * Reaction #2
        self.methane = Molecule(self.render, "C")
        self.water3 = Molecule(self.render, "O")
        self.monox = Molecule(self.render, "[C-]#[O+]")
        self.hydro1 = Molecule(self.render, "[H][H]")
        self.hydro2 = Molecule(self.render, "[H][H]")
        self.hydro3 = Molecule(self.render, "[H][H]")

        self.setup_reaction_1()
        self.setupt_reaction_2()

        self.all_molecule = [
            self.water1, self.water2, self.oxygen, self.hydrogen,
            self.methane, self.water3, self.monox, self.hydro1, self.hydro2, self.hydro3
        ]
        self.rotation_speed = 0.15
        self.custom_cam = Camera(self)
        self.setup_lighting()
        self.setBackgroundColor(56/255, 52/255, 53/255)
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

        title = Text3D(self.render, "Title1", "Réaction pour l'hydrogène vert", self.loader)
        title.set_position(5, 20, 4)

    def setupt_reaction_2(self):
        self.methane.build_molecule()
        self.methane.set_pos(0, 20, -10)

        plus1 = Text3D(self.render, "React2_plus1", "+", self.loader)
        plus1.set_position(2.5, 20, -10.5)

        self.water3.build_molecule()
        self.water3.set_pos(5, 20, -10)

        to = Text3D(self.render, "React2_to", ">", self.loader)
        to.set_position(7.5, 20, -10.5)

        self.monox.build_molecule()
        self.monox.set_pos(10, 20, -10)

        plus2 = Text3D(self.render, "React2_plus2", "+", self.loader)
        plus2.set_position(12.5, 20, -10.5)

        self.hydro1.build_molecule()
        self.hydro1.set_pos(15, 20, -8)
        self.hydro2.build_molecule()
        self.hydro2.set_pos(15, 20, -10)
        self.hydro3.build_molecule()
        self.hydro3.set_pos(15, 20, -12)

        title = Text3D(self.render, "Title2", "Réaction pour l'hydrogène gris", self.loader)
        title.set_position(7, 20, -6)
    
    def update_rotation(self, task):
        for i, mol in enumerate(self.all_molecule):
            h, p, r = mol.get_rot()
            self.all_molecule[i].set_rotation(h + self.rotation_speed, p + self.rotation_speed, r + self.rotation_speed)
        return task.cont

def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
