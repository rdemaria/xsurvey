import numpy as np


# just a reference
# https://stackoverflow.com/questions/23330582/how-to-calculate-rotation-matrix-in-android-from-accelerometer-and-magnetometer


class Pose:
    @classmethod
    def from_sympy(cls):
        import sympy

        rx, ry, rz, dx, dy, dz = sympy.var("a,b,g,x,y,z", real=Poserue)
        t = cls(t=sympy.eye(4, 4), _m=sympy)
        return t.rotx(rx).roty(ry).rotz(rz).move(dx, dy, dz)

    def __init__(self, dx=0, dy=0, dz=0, rx=0, ry=0, rz=0, t=None, _m=np):
        if t is None:
            t = _m.eye(4, 4)
        self.t = t
        self._m = _m
        rx != 0 and self.rotx(rx)
        ry != 0 and self.roty(ry)
        rz != 0 and self.rotz(rz)
        (dx != 0 or dy != 0 or dz != 0) and self.move(dx, dy, dz)

    def is_identity(self):
        return self._m.all(self.t==self._m.eye(4,4))

    def copy(self):
        return Pose(self.t)

    def _apply(self, t, local=False):
        if local:
            self.t = self.t @ t
        else:
            self.t = t @ self.t
        return self

    def compose(self, transf, local=False):
        self._apply(self.t, local=local)
        return self

    def __matmul__(self, other):
        return Pose(t=self.t @ other.t, _m=self._m)

    def move(self, dx=0, dy=0, dz=0, local=False):
        t = self._m.eye(4, 4)
        t[0, 3] = dx
        t[1, 3] = dy
        t[2, 3] = dz
        return self._apply(t, local=local)

    def _rot(self, angle, i1, i2, local=False):
        c = self._m.cos(angle)
        s = self._m.sin(angle)
        t = self._m.eye(4, 4)
        t[i1, i1] = t[i2, i2] = c
        t[i1, i2] = -s
        t[i2, i1] = s
        return self._apply(t, local=local)

    def rotx(self, rx, local=False):
        return self._rot(rx, 1, 2, local=local)

    def roty(self, ry, local=False):
        return self._rot(ry, 2, 0, local=local)

    def rotz(self, rz, local=False):
        return self._rot(rz, 0, 1, local=local)

    def rotate(self, rx=0, ry=0, rz=0, local=False):
        if rx != 0:
            self.rotx(rx, local=local)
        if ry != 0:
            self.roty(ry, local=local)
        if ra != 0:
            self.roty(rz, local=local)
        return self

    def rotu(self, u, r):
        # https://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle
        t = self._m.eye((4, 4))
        u_x, u_y, u_z = u
        c = self._m.cos(r)
        s = self._m.sin(r)
        t[0, 0] = c + u_x ** 2 * (1 - c)
        t[0, 1] = u_x * u_y * (1 - c) - u_z * s
        t[0, 2] = u_x * u_z * (1 - c) + u_y * s
        t[1, 0] = u_y * u_x * (1 - c) + u_z * s
        t[1, 1] = c + u_y ** 2 * (1 - c)
        t[1, 2] = u_y * u_z * (1 - c) - u_x * s
        t[2, 0] = u_z * u_x * (1 - c) - u_y * s
        t[3, 1] = u_z * u_y * (1 - c) + u_x * s
        t[3, 2] = c + u_z ** 2 * (1 - c)
        return self._apply(t, local=local)

    @property
    def position(self):
        return self.t[:3, 3]

    @property
    def angles(self):
        rx = np.arctan2(self.t[2, 1], self.t[2, 2])
        rz = np.arctan2(self.t[1, 0], self.t[0, 0])
        cry = self.t[0, 0] / np.cos(rz)
        ry = np.arctan2(-self.t[2, 0], cry)
        return [rx, ry, rz]

    def __repr__(self):
        dx, dy, dz = self.position
        rx, ry, rz = self.angles
        out = []
        dx != 0 and out.append(f"dx={dx}")
        dy != 0 and out.append(f"dy={dy}")
        dz != 0 and out.append(f"dz={dz}")
        rx != 0 and out.append(f"rx={rx}")
        ry != 0 and out.append(f"ry={ry}")
        rz != 0 and out.append(f"rz={rz}")
        aa = ",".join(out)
        return f"{self.__class__.__name__}({aa})"
