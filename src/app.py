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

        mol = Molecule(
            self.render,
            "[Ag+].[N+](=O)([O-])[O-]",
        )
        mol.build_molecule()
        mol.set_pos(0, 20, 0)

        text = Text3D(self.render, "Hi", "Hello, World", self.loader)
        text.set_position(0, 20, 5)

        self.custom_cam = Camera(self)
        self.setup_lighting()
        self.setBackgroundColor(0.8745, 0.9216, 0.9176)
        self.render.setShaderAuto()

        taskMgr.add(self.custom_cam.update, "camera-update")
        taskMgr.add(self.update_shader, "shader-update")

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

def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
