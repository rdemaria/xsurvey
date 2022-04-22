import setuptools
import sys

requirements = {"install": ["numpy"]}

setuptools.setup(
    name="xsurvey",
    version="0.0.0",
    description="Geometry package",
    author="Riccardo De Maria",
    author_email="riccardo.de.maria@cern.ch",
    url="https://github.com/rdemaria/xsurvey",
    packages=["xsurvey"],
    package_dir={"xsurvey": "xsurvey"},
    install_requires=requirements["install"],
)
