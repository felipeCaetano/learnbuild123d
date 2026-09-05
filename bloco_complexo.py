from build123d import *
from ocp_vscode import show

with BuildPart() as bloco_complexo:
    Box(40, 40, 40)
    
    # 1. Filtramos as arestas horizontais (que não estão paralelas a Z)
    # 2. Ordenamos por Z (as mais baixas primeiro, as mais altas por último)
    # 3. Pegamos o grupo final [-1] (as arestas da tampa superior)
    arestas_topo = bloco_complexo.edges().filter_by(Axis.Z, reverse=True).sort_by(Axis.Z)[-1]
    
    # Aplicando o chanfro correto em minúsculo!
    chamfer(arestas_topo, length=3)

show(bloco_complexo)
