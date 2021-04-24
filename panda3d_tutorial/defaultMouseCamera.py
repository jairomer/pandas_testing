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
        # x, y, z 
        #########################
        # x is right-left
        # y is near-far
        # z is top down
        #########################
        # Disable default camera control behaviour.
        #self.disableMouse()

        env = self.loadModel("models/environment")
        env.reparentTo(self.render)

game = MyGame()
game.run()
