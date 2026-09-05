from build123d import *
from ocp_vscode import *


loc = Location((10, 20, 0), (0, 0, 45))
cubo_movido = loc * Box(10, 10, 10)
show(cubo_movido)
