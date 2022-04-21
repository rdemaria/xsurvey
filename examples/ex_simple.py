import xsurvey as xs

s1 = xs.Entity("s1")

s1.add_part("upright").move(dx=1, dy=1)
s1.add_part("upleft").move(dx=1, dy=1)
s1.add_part("downright").move(dx=1, dy=1)
s1.add_part("downleft").move(dx=1, dy=1)
s1.move(dx=0.1)

print(s1.parts["upright"].position)
print(s1["upright"].position)

s2 = s1.clone(name="s2").move(dx=1).rotx(xs.deg(5))
s3 = s1.copy(name="s2").move(dx=1).rotx(xs.deg(5))

ss = xs.Entity(parts={1: s1, 2: s2, 3: s3})

print(ss[1]["upright"].position)
print(ss[2]["upright"].position)
print(ss[3]["upright"].position)
s1.parts['upright'].move(dx=0.1,dy=0.1)
print(ss[1]["upright"].position)
print(ss[2]["upright"].position)
print(ss[3]["upright"].position)

fig = xs.Canvas2D(projection="xy")
fig.style["Point"]={size: 0.1}
fig.style["s1"]={"color": "b"}
fig.style["s2"]={"color": "r"}
fig.add(ss)

s1.move(dy=.2)
fig.update()
