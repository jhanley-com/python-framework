# Python Framework for GitHub, Read-The-Docs, PyPI

This project is a framework for rapidly getting setup to create a Python project, use GitHub for source control, Read The Docs for documentation and PyPI for package distribution. This framework includes everything to get setup to publish in 10 minutes.

# Warning

This package is still being created. Ignore this repository until I am finished. I will remove this warning once this package is ready.

I will be deleting and recreating this project several times; do not clone or fork this project until complete as this will mess up your copy.

If you are curious, download the zip file (listed below). This project is public instead of private as this project also supports Read The Docs which requires a public GitHub project to autobuild the documentation.

# Documentation

**Read the documentation:**
- Python Framework <https://python-framework.readthedocs.io/>
- Python Framework <https://python-framework.jhanley.com/>

# Download this package

- Download a zip file:
<https://github.com/jhanley-com/python-framework/archive/master.zip>

- Git Clone:
git clone https://github.com/jhanley-com/python-framework.git

# Contents

**Directory: docs**

&nbsp;&nbsp;&nbsp;&nbsp;This directory holds the documenation for the Python Framework. Ignore this for your project.

**Directory: my-project**

&nbsp;&nbsp;&nbsp;&nbsp;This is the directory that holds your project and documentation. Rename this folder to match your project name. You can also copy this directory to your working directory and work from there.

**Directory: tools-linux**

&nbsp;&nbsp;&nbsp;&nbsp;This directory contains tools that I use to upload this project to GitHub.

**Directory: tools-linux**

&nbsp;&nbsp;&nbsp;&nbsp;This directory contains tools that I use to upload this project to GitHub.

**File: README.md**

&nbsp;&nbsp;&nbsp;&nbsp;This file is the README for the Python Framework. Ignore this file. The README for your project is in the directory my-project.

**File: LICENSE**

&nbsp;&nbsp;&nbsp;&nbsp;This file is the LICENSE for the Python Framework. Ignore this file. The LICENSE for your project is in the directory my-project.

# The following sections are work in progress.

Edit README.md and setup.py to fit your project name, version, license, etc.

# Setup Documentation

pip install sphinx

Change to the "docs" directory.

Edit documentation

Build documentation:
make html

Rename the package folder mypackage to your package name
Add your source files/packages to the your package directory.

Build your package:
- python setup.py sdist bdist_wheel

install PyPI twine package:
pip install -U twine

Upload your release to PyPI:
twine upload dist/*
