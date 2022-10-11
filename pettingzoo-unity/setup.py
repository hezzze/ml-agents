#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install
from pettingzoo_unity import __version__, __release_tag__

VERSION = __version__
EXPECTED_TAG = __release_tag__


class VerifyVersionCommand(install):
    """
    Custom command to verify that the git tag is the expected one for the release.
    Originally based on https://circleci.com/blog/continuously-deploying-python-packages-to-pypi-with-circleci/
    This differs slightly because our tags and versions are different.
    """

    description = "verify that the git tag matches our version"

    def run(self):
        tag = os.getenv("GITHUB_REF", "NO GITHUB TAG!").replace("refs/tags/", "")

        if tag != EXPECTED_TAG:
            info = "Git tag: {} does not match the expected tag of this app: {}".format(
                tag, EXPECTED_TAG
            )
            sys.exit(info)


setup(
    name="pettingzoo_unity",
    version=VERSION,
    description="Unity Machine Learning Agents PettingZoo Interface",
    license="Apache License 2.0",
    author="Unity Technologies",
    author_email="ML-Agents@unity3d.com",
    url="https://github.com/Unity-Technologies/ml-agents",
    packages=find_packages(),
    install_requires=[
        "gym==0.21.0",
        "pettingzoo==1.13.1",
        "numpy==1.21.2",
        f"mlagents_envs==0.28.0",
    ],
    cmdclass={"verify": VerifyVersionCommand},
)
