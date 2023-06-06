import pathlib
from setuptools import setup, find_packages
# The directory containing this file
HERE = pathlib.Path(__file__).parent


with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='fastapi-redis',
      version="1.0",
      description="POC",
      packages=find_packages(),
      install_requires=requirements,
      zip_safe=False)