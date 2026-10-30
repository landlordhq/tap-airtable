#!/usr/bin/env python
from setuptools import setup, find_packages


setup(name='tap-airtable',
      version='0.0.3',
      description='Singer.io tap for extracting data from the Airtable API',
      author='AIME Mentorinng',
      url='https://singer.io',
      classifiers=[
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.12',
          'Programming Language :: Python :: 3.13',
          'Programming Language :: Python :: 3.14',
          'Programming Language :: Python :: 3.15',
      ],
      python_requires='>=3.12',
      py_modules=['tap_airtable'],
      install_requires=[
          'python-slugify>=8,<10',
          'requests>=2.32,<3',
          'singer-python>=6.1,<7',
      ],
      entry_points='''
          [console_scripts]
          tap-airtable=tap_airtable:main
      ''',
      packages=find_packages(),
      include_package_data=True,
      )
