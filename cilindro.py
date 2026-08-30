from build123d import *
from ocp_vscode import *


with BuildPart() as solido:
    Cylinder(radius=5, height=8)
    with BuildSketch(solido.faces().sort_by(Axis.Z)[-1]):
        Circle(radius=3)
    extrude(amount=-8, mode=Mode.SUBTRACT)

show(solido.part)
