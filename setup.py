from setuptools import setup, find_packages
import os

version = '2.2'

setup(name='uwosh.themebase',
      version=version,
      description="An installable theme for Plone 4.2",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='theme uwosh UWO oshkosh',
      author='T. Kim Nguyen',
      author_email='nguyen@uwosh.edu',
      url='https://svn.it.uwosh.edu/svn/plone/Projects/uwosh.themebase/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uwosh'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
