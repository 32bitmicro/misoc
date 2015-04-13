#!/usr/bin/env python3

import sys, os
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README")).read()

required_version = (3, 3)
if sys.version_info < required_version:
    raise SystemExit("MiSoC requires python {0} or greater".format(
        ".".join(map(str, required_version))))

setup(
    name="misoclib",
    version="unknown",
    description="a high performance and small footprint SoC based on Migen",
    long_description=README,
    author="Sebastien Bourdeauducq",
    author_email="sb@m-labs.hk",
    url="http://m-labs.hk",
    download_url="https://github.com/m-labs/misoc",
    packages=find_packages(here),
    license="BSD",
    platforms=["Any"],
    keywords="HDL ASIC FPGA hardware design",
    classifiers=[
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "Environment :: Console",
        "Development Status :: Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
