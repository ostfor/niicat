from setuptools import setup, find_packages

with open("Readme.md", "r") as f:
    long_description = f.read()

setup(name='niicat',
      version='0.4.3',
      description='Preview nifti images on the terminal',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/MIC-DKFZ/niicat/',
      author='Jakob Wasserthal',
      author_email='j.wasserthal@dkfz.de',
      python_requires='>=2.7,<=3.8',
      license='GPL v2',
      packages=find_packages(),
      install_requires=[
          'nibabel==2.3.0',
          'matplotlib~=3.1',
          'numpy~=1.17.0',
          'libsixel-python'
      ],
      zip_safe=False,
      classifiers=[
          'Intended Audience :: Science/Research',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Operating System :: Unix',
          'Operating System :: MacOS'
      ],
      scripts=[
          'bin/niicat'
      ],
      package_data={'niicat.resources': ['imgcat.sh', 'niipre.py']},
)
