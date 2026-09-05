from build123d import *
from ocp_vscode import *



with BuildPart() as bloco_chanfrado:
    Box(40, 40, 40)
    
    # Filtra as faces que apontam puramente para cima (Eixo Z positivo)
    face_do_topo = bloco_chanfrado.faces().filter_by(Axis.Z)[-1] # Pega a mais alta em Z
    
    # Pegamos as arestas dessa face específica
    arestas_do_topo = face_do_topo.edges()
    
    chamfer(arestas_do_topo, length=3)


show(bloco_chanfrado.part)
