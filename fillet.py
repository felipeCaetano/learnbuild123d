from build123d import *
from ocp_vscode import *



with BuildPart() as bloco:
    Box(40, 40, 40)
    
    # 1. Pegamos TODAS as arestas: bloco.edges()
    # 2. Filtramos apenas as que estão paralelas ao Eixo Z: .filter_by(Axis.Z)
    arestas_verticais = bloco.edges().filter_by(Axis.Z)
    
    # 3. Aplicamos o arredondamento (Fillet) nelas
    fillet(arestas_verticais, radius=5)

show(bloco.part)
