from build123d import *
from ocp_vscode import show


with BuildPart() as part:
    with BuildSketch():
        Rectangle(90, 90)
    extrude(amount=60)
    chamfer(part.edges().filter_by(Axis.X, reverse=True)[-1], length=20)


show(part.part)

