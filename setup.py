from setuptools import setup

# sample from https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html
# refer further to https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#python-requires

setup(
   name='PE',
   # version='0.1.0',
   # author='An Awesome Coder',
   # author_email='aac@example.com',
   packages=["PE"],
   # scripts=['bin/script1','bin/script2'],
   # url='http://pypi.python.org/pypi/PackageName/',
   # license='LICENSE.txt',
   # description='PE code',
   # long_description=open('README.txt').read(),
   python_requires='>=3',
   # install_requires=[],
)

# install in develop/editable mode
# python setup.py develop
# pip install .
# It puts a link (actually *.pth files) into the python installation to your code, 
# so that your package is installed, but any changes will immediately take effect.