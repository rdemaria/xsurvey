import xsurvey as xs

def test_transformation():
    pose=xs.transformation.Pose()
    assert pose.is_identity()


