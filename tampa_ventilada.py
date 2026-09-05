from build123d import *
from ocp_vscode import *


with BuildPart() as tampa_ventilada:
    # 1. Base da tampa
    Box(120, 120, 5)
    
    # 2. Criamos uma grade de 5 colunas por 5 linhas
    # Cada furo estará espaçado em 20mm no eixo X e 20mm no eixo Y
    with GridLocations(20, 20, 5, 5):
        # Tudo criado aqui será replicado 25 vezes (5x5)
        # O build123d centraliza a grade automaticamente na origem atual
        Cylinder(radius=4, height=5, mode=Mode.SUBTRACT)


show(tampa_ventilada.part)
