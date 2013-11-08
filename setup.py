#!/usr/bin/env python
import os
from setuptools import setup, find_packages

# Utility function to read the README and VERSION files.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "contribution-counter",
    version = read("VERSION").strip(),
    author = "John Sullivan and other contributers",
    author_email = "jsull003@ucr.edu",
    description = "A tool for accessing contributions on GitHub.",
    license = "Apache v2.0",
    keywords = "GitHub, contributions, python",
    url = "https://www.github.com/brownhead/contribution-counter",
    long_description = read("README.md"),
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License"
    ],
    packages = find_packages(),
    zip_safe = False,
    data_files = [
        (".", ["LICENSE", "README.md", "VERSION"])
    ],
    install_requires = [
        "requests==2.0.1",
        "beautifulsoup4==4.3.2"
    ]
)
