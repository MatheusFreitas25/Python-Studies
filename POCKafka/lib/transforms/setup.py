import re
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


setup(
    name="transforms",
    url="https://github.com/kovihq/data-pipeline",
    packages=find_packages(include=["transforms"]),
    version="0.29",
    description="transforms functions",
    author="team analytics <analytics@kovi.us>",
    license="MIT",
    install_requires=[],
    long_description=read("README.md"),
    setup_requires=["shapely>=1.7.1", "pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="nose.collector",
)
