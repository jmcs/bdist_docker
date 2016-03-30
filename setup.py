
from setuptools import setup


def get_long_description():
    """
    Read long description in a way that doesn't break if README.rst doesn't exist (for example in the docker image)
    """
    try:
        description = open('README.rst').read()
    except FileNotFoundError:
        description = ''
    return description


setup(name='bdist_docker',
      version='0.1.1',
      description='Distutils extension command to build docker images for python applications.',
      long_description=get_long_description(),
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        ],
      author='João Santos',
      author_email='jmcs@jsantos.eu'
      url='https://github.com/jmcs/bdist_docker/',
      license='Apache License Version 2.0',
      install_requires=['wheel'],
      packages=['bdist_docker'],
      entry_points="""
[distutils.commands]
bdist_docker = bdist_docker:bdist_docker
"""
      )
