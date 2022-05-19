import dartpy as dart


class HelloWorldNode(dart.gui.osg.RealTimeWorldNode):
    # Use this function to execute custom code before each time that the
    # window is rendered. This function can be deleted if it does not need
    # to be used.
    def customPreRefresh(self):
        pass

    # Use this function to execute custom code after each time that the
    # window is rendered. This function can be deleted if it does not need
    # to be used.
    def customPostRefresh(self):
        pass

    # Use this function to execute custom code before each simulation time
    # step is performed. This function can be deleted if it does not need
    # to be used.
    def customPreStep(self):
        pass

    # Use this function to execute custom code after each simulation time
    # step is performed. This function can be deleted if it does not need
    # to be used.
    def customPostStep(self):
        pass


def main():
    pathname = "/home/swkokr/dartpy_sample/fullbody_simbicon/final result ver2(4.28)"

    world = dart.simulation.World()

    urdfParser = dart.utils.DartLoader()
    kr5 = urdfParser.parseSkeleton(pathname + "/fullbody.urdf")
    ground = urdfParser.parseSkeleton(pathname + "/ground.urdf")
    world.addSkeleton(kr5)
    world.addSkeleton(ground)
    world.setGravity([0, 0, -9.81])

    # Create world node and add it to viewer
    node = HelloWorldNode(world)

    # create a viewer with background color (red, green, blue, alpha), here: white
    #viewer = dart.gui.osg.Viewer([1.0, 1.0, 1.0, 1.0])
    viewer = dart.gui.osg.Viewer()
    viewer.addWorldNode(node)

    # Grid settings
    grid = dart.gui.osg.GridVisual()
    grid.setPlaneType(dart.gui.osg.GridVisual.PlaneType.XY)
    grid.setOffset([0, -0.55, 0])
    viewer.addAttachment(grid)

    viewer.setUpViewInWindow(0, 0, 1920, 1080)
    viewer.setCameraHomePosition([2.0, 1.0, 2.0],
                                 [0.00, 0.00, 0.00],
                                 [0, 0, 1])
    viewer.run()


if __name__ == "__main__":
    main()
