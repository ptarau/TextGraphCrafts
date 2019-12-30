import subprocess
from sys import platform
import os
from setuptools import setup

with open('requirements.txt') as f:
  required = f.read().splitlines()
with open("README.md", "r") as f:
  long_description = f.read()

version = "0.0.6"
setup(name='textcrafts',
      version=version,
      description='textcrafts: Summary, keyphrase and relation extraction with dependecy graphs',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/ptarau/TextGraphCrafts.git',
      author='Paul Tarau, Andrea Cortis',
      author_USER_EMAIL='<paul.tarau@gmail.com>; andrea.cortis@gmail.com>',
      license='Apache',
      packages=['textcrafts'],
      #package_data={'deep_talk': ['*.pro']},
      #include_package_data=True,
      install_requires=required,
      zip_safe=False
      )

