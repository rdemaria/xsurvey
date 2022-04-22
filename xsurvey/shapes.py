from .entity import Entity





class Cylinder(Entity):
    def __init__(self,radius=1,length=1,
            name=None, pose=None, parts=None, **extra):
        self.radius=radius
        self.length=length
        super().__init__(name,pose,parts,**extra)

    def render(self):





MT='MOVETO'
LT='LINETO'
C3='CURVE3'
C4='CURVE4'
CL='CLOSEPOLY'


class Point2D:
    def __init__(self,xy):
        if isinstance(Point2D,xy):
            self.xy=xy.xy
        elif len(xy)==2:
            self.xy
        else:
            raise ValueError(f"Point2d cannot be initialied by {xy}")

class Patch(Entity):
    self.name=None
    def __init__(self,name,vertices,codes,**style):
        if len(vertices)!=codes:
            raise ValueError(f"{vertices} and {codes} do not have the same length")
        self.parts={ii:Point2D for ii,pp in enumerate(vertices)}
        self.codes=codes
        self.style=style

class Square(Patch):
     markers=dict(NE=(0.5,0.5),NW=(-0.5,0.5),
               SW=(-0.5,-0.5),SE=(0.5,-0.5),
               O=(0,0),
               E=(0.5,0.0),N=(-0.0,0.5),W=(-0.5,-0.0),S=(0.0,-0.5))
     vertices=np.array([[0.5,0.5],[-0.5,0.5],[-0.5,-0.5],[0.5,-0.5],[0,0]])
     codes=[MT,LT,LT,LT,CL]

    def __init__(self,**style):
        Patch.__init__(self,Square.vertices,Square.codes,**opts)


