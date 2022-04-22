import copy

from .transformation import Pose

def applystyle(entity, style):
    if entity.name in style:
        return style[entity.name]
    if entity.layer in style:
        return style[entity.layer]
    elif entity.__class__.__name__ in style:
        return style[entity.__class__.__name__]
    return style


defaultstyle = {"Point": {"show": False}}


class Entity:
    def __init__(self, name=None, pose=None, parts=None, **extra):
        self.name = name
        if parts is None:
            parts = {}
        self.parts = parts
        if pose is None:
            pose = Pose()
        self.pose = pose
        self.__dict__.update(extra)

    # should be overwritten by subclasses
    def copy(self, name=None, pose=None):
        dct=self.__dict__.copy()
        if name is not None:
            dct["name"] = name
        if pose is not None:
            dct["pose"] = pose
        return self.__class__(**dct)

    def clone(self, name=None, pose=None, use_clone=False):
        if pose is None:
            pose=Pose()
        if use_clone:
            return Clone(self,name=name,pose=pose)
        else:
            return Entity(name=name,parts={None:self})

    def move(self, dx=0, dy=0, dz=0):
        self.pose.move(dx=dx, dy=dy,dz=dz)
        return self

    def rotate(self, rx=0,ry=0,rz=0):
        self.pose.rotate(rx=rx,ry=ry,rz=rz)
        return self

    def rotx(self,rx):
        self.pose.rotx(rx)
        return self

    def roty(self,rx):
        self.pose.roty(ry)
        return self

    def rotz(self,rx):
        self.pose.roty(ry)
        return self

    def rotu(self,u,r):
        self.pose.rotu(u,r)
        return self

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            try:
               part=self.parts[None]
               part=part.copy(name=self.name,pose=self.pose@part.pose)
               return getattr(part,key)
            except (KeyError,AttributeError):
                raise AttributeError(f"`{key}` not found in {self}")

    def __getitem__(self, key):
        part=self.parts[key]
        return part.copy(name=(self.name, key), pose=self.pose@part.pose)

    def render(self, pose=None, style=defaultstyle):
        if self.trans is None:
            raise ValueError("Entity {self.name} does not have a position")
        primitives = []
        for part in self.parts:
            primitives.extent
            for primi in part.render(applystyle(part, style)):
                primitives.append(primi.transform(self.trans))
        return primitives

    def add_part(self, name=None, part=None, pose=None):
        if part is None:
            part= Entity(name=name, pose=pose)
        self.parts[name] = part
        return part

    @property
    def position(self):
        return self.pose.position

    def __repr__(self):
        cname=self.__class__.__name__
        args=[]
        if self.name is not None:
            args.append(repr(self.name))
        if not self.pose.is_identity():
            args.append(repr(self.pose))
        #if self.parts:
        #    args.append('parts=...')
        args=' '.join(args)
        return f"<{cname} {args}>"



#hacky...
#Contrary to a copy if ref is updated, the clone follows
class Clone:
    classrepo={}
    def __init__(self,ref,**kwargs):
        self._ref=ref
        self.__dict__.update(kwargs)
        cls=ref.__class__
        clsname=cls.__name__+'Clone'
        bases=(Clone,cls)
        if bases in Clone.classrepo:
            cloneclass=Clone.classrepo[bases]
        else:
            cloneclass=type(cls.__name__+'Clone',bases,{})
            Clone.classrepo[bases]=cloneclass
        self.__class__=cloneclass

    def __getattr__(self,k):
        return getattr(self._ref,k)

