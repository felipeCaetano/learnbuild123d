from build123d import *
from ocp_vscode import *


with BuildPart() as boxes:
    Box(3, 2, 1)
    with BuildSketch(boxes.faces().sort_by(Axis.Z)[-1]):
        with Locations((-1, 0)):
            Rectangle(1, 1)
    extrude(amount=1)


show(boxes)
