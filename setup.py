from setuptools import setup

setup(name='rdrama',
      version='0.0.0',
      description='rdrama API Wrapper',
      long_description=open('README.rst').read(),
      url='https://github.com/ithinkimokay/rdrama',
      author='diogenesjunior',
      author_email='diogenesjunior@protonmail.com',
      packages=['rdrama'],
      zip_safe=False,
      keywords='rdrama API RAW',
      install_requires=['requests'],
      include_package_data=True
      )
