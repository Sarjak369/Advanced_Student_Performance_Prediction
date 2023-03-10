from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = "-e ."

# this function will return the list of requirements
def get_requirements(file_path: str) -> List[str]:

    requirements = []
    with open("requirements.txt") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="Advanced Student Performance Prediction ML Project",
    version="0.0.1",
    author="Sarjak",
    author_email="sarjakmaniar369@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)