from direct.showbase.ShowBase import ShowBase

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Disable the camera trackball controls.
        self.disableMouse()

def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()