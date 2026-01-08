from panda3d.core import Vec3
from direct.task import Task

class Camera:
    def __init__(self, base, init_speed=10.0, sensitivity=60.0):
        self.base = base
        self.camera = self.base.camera
        self.dt = 0
        self.set_dt()

        self.speed = init_speed
        self.sensitivity = sensitivity

        self.keys = {
            "w": False, 
            "s": False,
            "a": False, 
            "d": False,

            "arrow_up": False,
            "arrow_down": False,
            "arrow_left": False,
            "arrow_right": False,
        }
        
        self.camera.setPos(0, 0, 0)
        self.camera.lookAt(0, 0, 0)

        for k in self.keys:
            base.accept(k, self.set_key, [k, True])
            base.accept(f"{k}-up", self.set_key, [k, False])
    
    def set_key(self, key, value):
        self.keys[key] = value
    
    def set_dt(self):
        self.dt = globalClock.get_dt()
    
    def moveCamera(self):
        direction = Vec3(0, 0, 0)

        if self.keys["w"]: direction.y += 1
        if self.keys["s"]: direction.y -= 1
        if self.keys["a"]: direction.x -= 1
        if self.keys["d"]: direction.x += 1

        self.camera.setPos(self.camera, direction * self.speed * self.dt)
    
    def rotateCamera(self):
        h, p, r = self.camera.getHpr()

        if self.keys["arrow_up"]: 
            p += self.sensitivity * self.dt
        if self.keys["arrow_down"]: 
            p -= self.sensitivity * self.dt
        if self.keys["arrow_left"]:
            h += self.sensitivity * self.dt
        if self.keys["arrow_right"]: 
            h -= self.sensitivity * self.dt

        p = max(-89, min(89, p))

        self.camera.setHpr(h, p, r)
    
    def update(self, task):
        self.set_dt()
        self.moveCamera()
        self.rotateCamera()
        return Task.cont
    