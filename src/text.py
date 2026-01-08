from panda3d.core import TextNode

class Text3D:
    def __init__(self, render, id, content, loader, font="cmtt12"):
        self.render = render
        self.loader = loader

        self.text = TextNode(id)
        self.text.setText(content)
        self.text.setAlign(TextNode.ACenter)
        self.text.setFont(self.loader.loadFont("cmtt12"))  # optional font

        self.root = self.render.attachNewNode(self.text)
    
    def set_position(self, x=0, y=0, z=0):
        self.root.setPos(x, y, z)
    
    def set_rotation(self, h=0, p=0, r=0):
        self.root.setHpr(h, p, r)
    
    def set_scale(self, scale=1):
        self.root.setScale(scale)