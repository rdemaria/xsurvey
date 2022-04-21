import xsurvey as xs


s1 = xs.Cylinder(radius=3, length=2)
s2 = xs.Tube(innersection=xs.Square(2).rotation(xs.deg(30)), thickness=0.1, length=2)

s3 = xs.Cylinder(radius=1, lenght=2, angle=0.12).roty(xs.deg(0.2))
s4 = xs.Tube(outerradius=1.2, thickness=0.1, lenght=2, angle=0.12)

m1 = xs.Entity(parts={"field": s1, "beamscreen": s2})
m2 = xs.Entity(parts={"field": s3, "beamscreen": s4})

a1 = xs.Entity(parts={"m1": m1.zshift(-2), "m2": m2.zshift(2)})

line = xs.BeamLine()
line.add("st", xs.Point(), at=0)
line.add("a1.1", a1, at=3, from_=st)
line.add(
    "a1.2",
    a1,
    at=3,
    at_ref="start",
    from_="a1.1",
    from_ref="end",
    align=xs.YRotation(0.1),
    align_ref="center",
)
line.build()  # reference cannot be changed
line.modify()  # poses invalidated
line.parts["a1.2"].at+=0.1
line.build()  # reference cannot be changed

print(line['a1.2'].m1.field.start.position) # global position
print(line.parts['a1.2'].m1.beam.end.position) # local position

scene = line.render()

scene.drawTopView({"bpm": {"show": False}}, {"beamscreen": {"edgecolor": "green"}})
