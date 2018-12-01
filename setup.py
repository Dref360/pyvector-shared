from setuptools import setup
from setuptools import find_packages

long_description = '''
Implementation of a sharable vector-like structure.
'''

setup(name='PyVector',
      version='0.0.1',
      description='',
      long_description=long_description,
      author='Frédéric Branchaud-Charron',
      author_email='frederic.branchaud.charron@gmail.com',
      url='https://github.com/Dref360/pyvector-shared',
      license='MIT',
      install_requires=['numpy>=1.9.1'],
      extras_require={
          'tests': ['pytest',
                    'pytest-pep8',
                    'pytest-xdist'],
      },
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=find_packages())
