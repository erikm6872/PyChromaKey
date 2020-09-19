import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyChromaKey",
    version="0.0.1",
    author="Erik McLaughlin",
    author_email="erik@erikcmclaughlin.com",
    description="Chroma key (green screen) library for Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erikm6872/PyChromaKey",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)