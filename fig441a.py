from build123d import *
from ocp_vscode import *

with BuildPart() as part:
    Box(4,2,3)
    with Locations((0,0.5,.75)):
        Box(4,1,1.5, mode=Mode.SUBTRACT)


show(part.part)
