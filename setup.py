import subprocess
from sys import platform
import os
from setuptools import setup

if __name__ == '__main__':

    with open('requirements.txt') as f:
        required = f.read().splitlines()

    with open("README.md","r") as f:
        long_description = f.read()

    version = "0.0.2_a"
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


    def _post_install(setup):
        def _post_actions():
            print ('--- Post install ---')
            # import nltk
            # import platform
            # if platform.system()=='darwin':
            #     try:
            #         import ssl
            #         _create_unverified_https_context = ssl._create_unverified_context
            #     except AttributeError:
            #         pass
            #     else:
            #         ssl._create_default_https_context = _create_unverified_https_context
            # nltk.download()

        _post_actions()
        return setup

    setup = _post_install(
          setup(name='text_graph_crafts',
          version=version,
          description='DeepRank Model: a deep learning approach to relevance ranking in information retrieval ',
          long_description = long_description,
          long_description_content_type='text/markdown',
          url='https://github.com/ptarau/TextGraphCrafts.git',
          author='Paul Tarau, Andrea Cortis',
          author_USER_EMAIL='<paul.tarau@gmail.com>; andrea.cortis@gmail.com>',
          license='Apache',
          packages=['text_graph_crafts'],
          install_requires = required,
          zip_safe=False,
          setup_requires = ['nltk'],
          )
)
