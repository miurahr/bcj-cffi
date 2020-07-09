#!/usr/bin/env python

from setuptools import setup

setup(use_scm_version={"local_scheme": "no-local-version"},
      cffi_modules=["bcj_builder.py:ffibuilder"])