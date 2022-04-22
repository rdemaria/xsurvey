import xsurvey as xs


class Magnet(xs.Entity):
    def __init__(self,name=None,length=0,angle=0,tilt=0,
                      pose=None,parts=None,**extra):
        self.length=length
        self.angle=angle
        self.tilt=tilt
        if parts is None:
           parts={}
           parts['start']=xs.Entity().move(dz=-length/2)
           parts['end']=xs.Entity().move(dz=+length/2)
        super().__init__(name,pose,parts,**extra)

    def info(self):
        print("a")


mb=Magnet("MB",length=3)

mb1=mb.clone("MB1").move(dx=1)


