from build123d import *
from ocp_vscode import show


with BuildPart() as part:
    with BuildSketch():
        with BuildLine():
            poli = Polyline(
                (0,0), (90,0), (90,30), (50,30), (50,40),
                (25,40), (25,25), (0,25), (0,0)
                )
        make_face()
    revolve(axis=Axis.X)
    circular_edges = part.edges().filter_by(GeomType.CIRCLE)
    fillet(circular_edges, radius=1)


show(part.part)
