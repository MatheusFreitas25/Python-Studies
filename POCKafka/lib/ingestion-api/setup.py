import re
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


setup(
    name="ingestion",
    url="https://github.com/kovihq/data-pipeline",
    packages=find_packages(include=["ingestion"]),
    version="1.0",
    description="ingestion functions",
    author="team analytics <analytics@kovi.us>",
    license="MIT",
    install_requires=[],
    long_description=read("README.md"),
    setup_requires=["requests", "pytest-runner"],
    tests_require=["requests==2.22.0", "pytest==4.4.1"],
    test_suite="nose.collector",
)
