#!usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages

setup(
        name             = "keras-learn",
        version          = "0.0.1",
        description      = "",
        license          = "BSD-2-Clause",
        author           = "gen/5",
        author_email     = "gen_fifth@outlook.jp",
        url              = "https://github.com/genfifth/keras-learn.git",
        packages         = find_packages(),
        install_requires = ["Keras>=2.1.2", 
                            "pydot-ng>=1.0.0", 
                            "tensorflow>=1.4.1", 
                            "ipython>=6.1.0"
                            "ipwidgets>=7.0.0"],
        )