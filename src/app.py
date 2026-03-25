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

        # * Test Molecule
        self.test = Molecule(self.render, "FC(CC(C(C1(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(C(CC2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)(C2Cl)C2I)Br)F)C2Cl)I)Cl)C1Br")
        self.test.build_molecule()
        self.test.set_pos(0, 20, 50)
        
        self.setup_reaction_1()
        self.setupt_reaction_2()

        self.all_molecule = [
            self.water1, self.water2, self.oxygen, self.hydrogen,
            self.methane, self.water3, self.monox, self.hydro1, self.hydro2, self.hydro3,
            self.test
        ]

        self.show = [
            (0, 5, 20, 0.75), (1, 0, 20, 1), (1, 5, 20, 0.75), (1, 10, 20, 0.75),
            (0, 7.5, 20, -15.5), (1, 0, 20, -15), (1, 5, 20, -15), (1, 10, 20, -15), (1, 15, 20, -15),
            (0, 0, 20, 50),
        ]
        self.show_idx = 0

        self.rotation_speed = 0.15
        self.custom_cam = Camera(self)
        self.update_cam_pos()

        self.setup_lighting()
        self.setBackgroundColor(56/255, 52/255, 53/255)
        self.render.setShaderAuto()

        taskMgr.add(self.custom_cam.update, "camera-update")
        taskMgr.add(self.update_shader, "shader-update")

        taskMgr.add(self.update_rotation, "rotation-update")
        taskMgr.add(self.update_show, "rotation-update")

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
        self.methane.set_pos(0, 20, -15)

        plus1 = Text3D(self.render, "React2_plus1", "+", self.loader)
        plus1.set_position(2.5, 20, -15.5)

        self.water3.build_molecule()
        self.water3.set_pos(5, 20, -15)

        to = Text3D(self.render, "React2_to", ">", self.loader)
        to.set_position(7.5, 20, -15.5)

        self.monox.build_molecule()
        self.monox.set_pos(10, 20, -15)

        plus2 = Text3D(self.render, "React2_plus2", "+", self.loader)
        plus2.set_position(12.5, 20, -15.5)

        self.hydro1.build_molecule()
        self.hydro1.set_pos(15, 20, -13)
        self.hydro2.build_molecule()
        self.hydro2.set_pos(15, 20, -15)
        self.hydro3.build_molecule()
        self.hydro3.set_pos(15, 20, -17)

        title = Text3D(self.render, "Title2", "Réaction pour l'hydrogène gris", self.loader)
        title.set_position(7, 20, -11)
    
    def update_rotation(self, task):
        for i, mol in enumerate(self.all_molecule):
            h, p, r = mol.get_rot()
            self.all_molecule[i].set_rotation(h + self.rotation_speed, p + self.rotation_speed, r + self.rotation_speed)
        return task.cont
    
    def next(self):
        self.show_idx = self.show_idx + 1 if self.show_idx < len(self.show)-2 else 0
        self.update_cam_pos()

    def back(self):
        self.show_idx = self.show_idx - 1 if self.show_idx > 0 else len(self.show)-2
        self.update_cam_pos()
    
    def test_mol(self):
        self.show_idx = len(self.show)-1
        self.update_cam_pos()

    def update_cam_pos(self):
        idx = self.show_idx
        set_back = -7 if not self.show[idx][0] else 10
        self.custom_cam.camera.setPos(self.show[idx][1], set_back, self.show[idx][3])
        self.custom_cam.camera.lookAt(self.show[idx][1], self.show[idx][2], self.show[idx][3])

    def update_show(self, task):
        self.accept("n", self.next)
        self.accept("mouse1", self.next)

        self.accept("b", self.back)
        self.accept("mouse3", self.back)

        self.accept("m", self.test_mol)
        self.accept("mouse2", self.test_mol)

        return task.cont

def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
