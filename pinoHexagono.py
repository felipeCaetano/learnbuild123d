from build123d import *
from ocp_vscode import *


with BuildPart() as solido:
    with BuildSketch():
        RegularPolygon(radius=4, side_count=6)
    extrude(amount=2)
    with BuildSketch(solido.faces().sort_by(Axis.Z)[-1]):
        Circle(radius=2)
    extrude(amount=3)
    Hole(radius=1)


show(solido.part)
