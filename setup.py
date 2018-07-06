from setuptools import setup, find_packages

setup(name='cavparams',
      version='0.1',
      description='Simple estimators of FP cavity parameters',
      #url='http://github.com/storborg/funniest',
      author='Michele Valentini',
      author_email='michele.valentini@unitn.it',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'numpy',
      ])
