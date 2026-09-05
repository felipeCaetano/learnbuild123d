from build123d import *
from ocp_vscode import *

LADO_MAIOR = 10
ALTURA = 30

with BuildPart() as part:
    with BuildSketch(Plane.XZ):
        with BuildLine() as trapezio:
            Polyline(
                (LADO_MAIOR / 2, 0),
                (LADO_MAIOR, 0),
                (LADO_MAIOR, ALTURA),
                (0, ALTURA),
                close=True)
        make_face()
    extrude(amount=ALTURA)


show(part.part)
