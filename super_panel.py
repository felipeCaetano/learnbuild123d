from build123d import *
from ocp_vscode import *


with BuildPart() as super_painel:
    Box(300, 300, 5)
    
    # Cria 4 pontos centrais usando uma grade de 2x2
    with GridLocations(150, 150, 2, 2):
        # A partir de CADA UM desses 4 pontos, cria um anel de furos circulares
        with PolarLocations(radius=25, count=8):
            Cylinder(radius=3, height=5, mode=Mode.SUBTRACT)


show(super_painel.part)
