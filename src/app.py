from direct.showbase.ShowBase import ShowBase

from camera import *
from molecule import *
from text import *
from reader import *

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Disable the camera trackball controls.
        self.disableMouse()

        self.reader = MVReader(self.render, self.loader, "scripts/test.mvs")
        self.reader.analyze()
        self.reader.execute()

        self.custom_cam = Camera(self)

        taskMgr.add(self.custom_cam.update, "camera-update")

        #self.render.ls()

def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
