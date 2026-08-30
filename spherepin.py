from build123d import *
from ocp_vscode import *


with BuildPart() as spherepin:
    Cylinder(radius=3, height=5)
    with Locations((0,0, 5)):
        Sphere(radius=4)

show_all()
