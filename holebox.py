from build123d import *
from ocp_vscode import *

with BuildPart() as holeBox:
    Box(4, 4, 3)
    with BuildSketch(holeBox.faces().sort_by(Axis.Z)[-1]):
        Circle(radius=2)
    extrude(amount=-3, mode=Mode.SUBTRACT)

show(holeBox)
