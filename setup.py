from distutils.core import setup
from setuptools import find_packages

setup(
  name="snowflake",
  version="0.1",
  author="DSSS_ex5_kindler",
  author_email="flora.kindler@fau.de",
  packages=find_packages(),
  install_requires=["numpy","turtles"],
)
