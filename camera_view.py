from direct.showbase.ShowBase import ShowBase

import mouse

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setUpScene()

        # Disable default mouse system.
        base.disableMouse()

    def setUpScene(self):
        # Load testing environment.
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)

    def setUpUIControl(self):
        self.taskMgr.add(self.turnCameraTask, "TurnCameraTask")
        self.taskMgr.add(self.moveCameraTask, "MoveCameraTask")

    def turnCameraTask(self, task):
        # Set orientation of the camera with the mouse.
        #angleDegreesDeltaPF = task.time * 16.0
        #angleRadiansDeltaPF = angleDegrees * (pi / 180.0)
        #TODO: Figure out how to change the camera orientation.

        self.camera.setHpr(angleDegrees, 0, 0)

    def moveCameraTask(self, task):
        # Set location of the camera via WASD keys.


app = MyApp()
app.run()
