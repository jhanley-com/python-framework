import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jhanley-python-framework",
    version="0.1.0",
    author="John J. Hanley",
    author_email="blog@jhanley.com",
    description="Python Framwork",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jhanley-com/doc-test-2",
    packages=setuptools.find_packages(),
    platforms=['any'],
    license='MIT License',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
