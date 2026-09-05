from build123d import *
from ocp_vscode import *

altura_base=20
largura=60
profundidade_total = 60
profundidade_topo = 30
altura_parede_topo = 15
altura_telhado = 15
chanfro = 15


with BuildPart() as part:
    with BuildSketch() as base:
        Rectangle(largura, profundidade_total, align=(Align.CENTER, Align.MIN))
        vertices_frontais = base.vertices().group_by(Axis.Y)[0]
        chamfer(vertices_frontais, length=chanfro)
    extrude(amount=altura_base)

    with BuildSketch(Plane.XZ.offset(-profundidade_total)) as parede:
        with BuildLine():
            p1 = (-largura / 2, altura_base)
            p2 = (largura / 2, altura_base)
            p3 = (largura / 2, altura_base + altura_parede_topo)
            p4 = (0, altura_base + altura_parede_topo + altura_telhado)
            p5 = (-largura / 2, altura_base + altura_parede_topo)

            Polyline(p1,p2,p3,p4,p5, close=True)
        make_face()
    extrude(amount=profundidade_topo)


show(part.part)
