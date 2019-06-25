#!/usr/bin/env python3
from setuptools import setup


setup(
    name="drumbot",
    version="1.0",
    author="tilda",
    author_email="tda@lmao.tf",
    description=("Drumbot API wrapper for Python."),
    license="MIT",
    keywords="drumbot github noopschallenge",
    url="https://github.com/utilefordiscord/drumbot-implementation",
    packages=['drumbot'],
    long_description="Drumbot API wrapper for Python.",
    install_requires=['aiohttp'],
    classifiers=[
        "Development Status :: 5 - Release",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
