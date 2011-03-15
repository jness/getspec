from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='getspec',
      version=version,
      description="Tool for getting SPEC and Changelogs from IUS Packages",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Jeffrey Ness',
      author_email='jeffrey.ness@rackspace.com',
      url='',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
            'console_scripts': ['getspec = getspec.main:main']
        },
      )
