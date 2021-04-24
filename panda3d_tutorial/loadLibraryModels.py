from panda3d.core import loadPrcFile
loadPrcFile("config/config.prc")

from direct.showbase.ShowBase import ShowBase

class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        # Use model from library installed with pip.
        box = self.loader.loadModel("models/box")
        box.reparentTo(self.render)
        box.setPos(0, 10, 0)
        # Horizontal, Into the cammera, Vertical


game = MyGame()
game.run()
