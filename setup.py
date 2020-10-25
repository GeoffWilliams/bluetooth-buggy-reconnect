#!/usr/bin/python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bluetooth-buggy-reconnect",
    version="1",
    author="Yuri Konotopov",
    author_email="ykonotopov@gnome.org",
    description="Automatically connect to trusted buggy bluetooth devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nE0sIghT/bluetooth-buggy-reconnect",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'PyGObject'
    ],
    scripts=['bluetooth-buggy-reconnect']
)
