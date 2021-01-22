import setuptools
from os import path
import sys

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'flame_classification', '_version.py')) as version_file:
    exec(version_file.read())
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flame_classification",
    version=__version__,
    author="Seyed Navid Roohani Isfahani",
    author_email="navidroohani@gmail.com",
    description="micro flame classification library - CoOptima",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/navidroo/image_classification",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
	install_requires=[
        'numpy',
        'keras',
        'matplotlib',
        'tensorflow',
        'h5py',
		'pandas',
		'pydot'],
	include_package_data= True,
)