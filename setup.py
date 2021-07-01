from setuptools import setup, find_packages

setup(name='rdrama',
      version='0.0.0',
      author='diogenesjunior',
      author_email='diogenesjunior@protonmail.com',
      description='rdrama.net api wrapper',
      long_description=open('README.rst').read(),
      url='https://github.com/ithinkimokay/rdrama',
      packages=find_packages(),
      install_requires=['requests'],
      keywords='rdrama API wrapper',
      zip_safe=True)
