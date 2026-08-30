from build123d import *
from ocp_vscode import *

with BuildPart() as part:
    with BuildSketch():
        with BuildLine() as line:
            CenterArc(
                center=(-1.25,0), radius=1.25, start_angle=180, arc_size=180
                )
            Line((0,0), (2.5,0))
            Line((2.5,0), (2.5,3))
            Line((2.5,3), (-2.5,3))
            Line((-2.5,3), (-2.5,0))
        make_face(line.line)
    extrude(amount=3)
    with Locations((-1.25,0)):
        Hole(radius=.5)
    with Locations((1.25,1,2.5)):
        Box(2.5,2,1, mode=Mode.SUBTRACT)
    with Locations(part.faces().sort_by(Axis.Y)[-1]):
        with Locations((-1.25,-.5, 1)):
            with GridLocations(1.25,1, 2, 1):
                Hole(radius=.25)
            
    
show(part.part)
