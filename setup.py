#!/usr/bin/env python

import codecs
import os

from setuptools import find_packages
from setuptools import setup

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

install_requires = [
    'python_version >= "3.10"',
    "bpy",
]

version = None
exec(open("bpyhelpers/version.py").read())

long_description = ""
with codecs.open("./README.md", encoding="utf-8") as readme_md:
    long_description = readme_md.read()

setup(
    name="bpyhelpers",
    version=version,
    description="Helpers for the python Blender API (bpy)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VCityTeam/bpyhelpers",
    project_urls={
        "Source": "https://github.com/VCityTeam/bpyhelpers",
        "Tracker": "https://github.com/VCityTeam/bpyhelpers/issues",
    },
    packages=find_packages(exclude=["tests.*", "tests"]),
    python_requires=">=3.10",
    zip_safe=False,
    classifiers=[
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    maintainer="vcity_devel",
    maintainer_email="vcity@liris.cnrs.fr",
)
