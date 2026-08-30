from build123d import *
from ocp_vscode import *


with BuildPart() as flatpin:
    Cylinder(radius=5, height=2)
    with BuildSketch(flatpin.faces().sort_by(Axis.Z)[-1]):
        Circle(radius=4)
    extrude(amount=6)


show(flatpin.part)
