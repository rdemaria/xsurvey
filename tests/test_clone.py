from xsurvey.entity import Clone

def test_clone():
    class AClass:
        def __init__(self,v=4):
            self.v=v

        def mee(self):
            return self.v*2

    a=AClass(v=2)
    ca=Clone(a)
    assert ca.mee()==a.mee()
    ca.v=3
    assert ca.mee()!=a.mee()
    assert isinstance(ca,Clone)
    assert isinstance(ca,AClass)


