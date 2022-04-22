import xsurvey as xs


m=xs.Entity('Magnet',length=40, angle=0.1, tilt=0)
m.add_part('BeamPipe',xs.Cylinder(radius=.3,length=m.length+1.5))
m.add_part('Vessel',xs.Cylinder(radius=1.2,length=m.length+0.8))
m.add_part('FlangeL',xs.Cylinder(radius=.5,length=0.2)).move(dz=-m.length/2-0.1)
m.add_part('FlangeR',xs.Cylinder(radius=.5,length=0.2)).move(dz=m.length/2+0.1)


l=xs.BeamLine('PS')

l.add(m.clone('m1').move(dz=0.1), 4)
l.add(m.clone('m2').move(dz=0.1), 14)
l.add(m.clone('m3').move(dz=0.1), 24)

canvas=xs.Canvas2d(projection='xz')
canvas.add(l)

