#!/usr/bin/env python
from setuptools import setup, find_packages
import sys
import os

from importlib.metadata import version, PackageNotFoundError


try:
    if int(version("pip").split('.')[0]) < 6:
        print('pip older than 6.0 not supported, please upgrade pip with:\n\n'
              '    pip install -U pip')
        sys.exit(-1)
except PackageNotFoundError:
    pass

if os.environ.get('CONVERT_README'):
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
else:
    long_description = ''

version = sys.version_info[:2]
if version < (3, 8):
    print('thefuck requires Python version 3.8 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)

VERSION = '3.32'

install_requires = ['psutil', 'colorama']
extras_require = {":sys_platform=='win32'": ['win_unicode_console']}

if sys.platform == "win32":
    scripts = ['scripts\\fuck.bat', 'scripts\\fuck.ps1']
    entry_points = {'console_scripts': [
                  'thefuck = thefuck.entrypoints.main:main',
                  'thefuck_firstuse = thefuck.entrypoints.not_configured:main']}
else:
    scripts = []
    entry_points = {'console_scripts': [
                  'thefuck = thefuck.entrypoints.main:main',
                  'fuck = thefuck.entrypoints.not_configured:main']}

setup(name='thefuck',
      version=VERSION,
      description="Magnificent app which corrects your previous console command",
      long_description=long_description,
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/thefuck',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples',
                                      'tests', 'tests.*', 'release']),
      include_package_data=True,
      zip_safe=False,
      python_requires='>=3.8',
      install_requires=install_requires,
      extras_require=extras_require,
      scripts=scripts,
      entry_points=entry_points)
