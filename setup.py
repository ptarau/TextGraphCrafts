import subprocess
from sys import platform

import atexit
import os
import sys
from setuptools import setup
from setuptools.command.install import install

class CustomInstall(install):
    """
    https://exceptionshub.com/post-install-script-with-python-setuptools.html
    """
    def run(self):
        def _post_install():
            import nltk
            import ssl
            try:
                _create_unverified_https_context = ssl._create_unverified_context
            except AttributeError:
                pass
            else:
                ssl._create_default_https_context = _create_unverified_https_context
            nltk.download()
        atexit.register(_post_install)
        install.run(self)


if __name__ == '__main__':

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
          license='Apache',
          packages=['text_graph_crafts'],
          install_requires = required,
          zip_safe=False,
          cmdclass={'install': CustomInstall})
