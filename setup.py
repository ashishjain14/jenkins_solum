from distutils.core import setup
from setuptools import find_packages
setup(
     name='js',
     version='1.0',
     packages=find_packages(),
     entry_points={
         'console_scripts':[
             'japi = jenkins.git.api:main'
         ]

     },
     include_package_data=True,
     author='wipro'
)