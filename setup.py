from setuptools import setup, find_packages

version = '0.1'

setup(name='extragen',
      version=version,
      description="",
      long_description=open('README.rst').read(),
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      package_dir={'': 'src'},
      packages=find_packages('src', exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ])
