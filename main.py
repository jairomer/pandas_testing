from math import pi, sin, cos
from direct.task import Task
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import loadPrcFile
# Concepts
# - Scenes
# - Tasks: Logic to be executed each timeframe.
# - Actor
# - Interval: Task that change a property from one value to another over a specified period of time.
# - Sequence: Or metaintervals are a type of interval that contains other intervals.


class MyApp(ShowBase):

  #  def setupModelCache(self):
  #      self.configurationManager = ConfigVariableManager.getGlobalPtr()
  #      cacheDirVariable = self.configurationManager.makeVariable("model-cache-dir")
  #      currentWorkingDir = os.getcwd()
  #      if ".cache" not in os.listdir():
  #          os.mkdir(currentWorkingDir + "/.cache")

  #      cacheDirVariable.setDefaultValue(currentWorkingDir + ".cache")
  #      self.configurationManager.setValue(cacheDirVariable)

    def __init__(self):
        ShowBase.__init__(self)
        #self.setupModelCache()
        #loadPrcFile("config/Config.prc")
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        # As long as the procedure returns the constant AsyncTask.DS_cont
        # then the task manager will continue to call it every frame.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor
       # self.playerModel = self.loader.loadModel("/home/neusynk/Workspace/experiments/pandas_testing/models/HidrogenCapsule.gltf")
       # self.playerModel.setScale(0.005, 0.005, 0.005)
       # self.playerModel.reparentTo(self.render)
        self.pandaActor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation
        self.pandaActor.loop("walk")

        # Create the four lerp intervals needed for the panda to walk back and forth.
        posInterval1 = self.pandaActor.posInterval(13,
                                                   Point3(0,-10,0),
                                                   startPos=Point3(0, 10, 0))
        posInterval2 = self.pandaActor.posInterval(13,
                                                   Point3(0, 10,0),
                                                   startPos=Point3(0, -10, 0))

        hprInterval1 = self.pandaActor.hprInterval(3,
                                                   Point3(180,0,0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor.hprInterval(3,
                                                   Point3(0,0,0),
                                                   startHpr=Point3(180, 0, 0))

        self.pandaPace = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace")
        self.pandaPace.loop()

    # Define a procedure to move the camera.
    # We will compute the desired position of the camera based on how
    # much time has elapsed.
    # The camera rotates 6 degrees every second.
    def spinCameraTask(self, task):
        # 6.0 degrees per frame.
        angleDegrees = task.time * 16.0
        # Convert camera movement to degrees.
        angleRadians = angleDegrees * (pi / 180.0)
        # Set the position of the camera -> (X, Y, Z)
        # Y is horizontal and Z is vertical, X is for depth.
        self.camera.setPos(20*sin(angleRadians), -20*cos(angleRadians), 3)
        # Set the orientation of the camera.
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

app = MyApp()
app.run()
