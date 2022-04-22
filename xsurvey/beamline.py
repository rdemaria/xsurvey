from .entity import entity
from .transformation import Pose
from .entity import Entity

class Node(Entity):
    def __init__(self, beamline=None, at=0, from_=None,
                       name=None, pose=None):
        self.extratrans=extratrans
        self.from_=from_   # (entity, part)
        self.at=at
        self.beamline.add(self)
        self.t=None #None until beamline

    def __setattr__(self,k,v):
        if self.trans is not None:
            msg=f"Cannot set {k} in {self}, invalidate beam line first"
            raise AttributeError(msg)
        else:
            super().__setattr__(self,k,v)


class BeamLine(Entity):
    def calculate_poses(self):
        #place t in nodes

    def add(self,entity,from_, at, from_=None, extratrans=None):
        node=Node(from_, at, extratrans)
        self.parts[entity.name]=Node(from_, at, extratrans)
        self.invalidate_trans()
        return 

    def remove(self,name):
        del self.nodes[name]
        self.invalidate_trans()


