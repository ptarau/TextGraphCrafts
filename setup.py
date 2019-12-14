from setuptools import setup
import subprocess


with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md","r") as f:
    long_description = f.read()


version = "0.0.1"
RELEASE_VERSION = True

if not RELEASE_VERSION:
    # Append incremental version number from git
    try:
        version += (
            ".dev"
            + subprocess.check_output(["git", "rev-list", "--count", "HEAD"])
            .decode()
            .strip()
        )
        print(f'version = {version}')
    except (subprocess.CalledProcessError, FileNotFoundError):
        # The .git directory has been removed (likely by setup.py sdist),
        # and/or git is not installed
        version += ".dev0"
        print(f'version = {version}')



setup(name='text_graph_crafts',
      version=version,
      description='DeepRank Model: a deep learning approach to relevance ranking in information retrieval ',
      long_description = long_description,
      url='https://github.com/ptarau/TextGraphCrafts.git',
      author='Paul Tarau, Andrea Cortis',
      author_USER_EMAIL='<paul.tarau@gmail.com>; andrea.cortis@gmail.com>',
      license='GNU GENERAL PUBLIC LICENSE Version 3',
      packages=['text_graph_crafts'],
      install_requires = required,
      zip_safe=False)
