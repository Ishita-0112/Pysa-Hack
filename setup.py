from setuptools import setup

with open("README.md", "r") as fh: 
    long_description = fh.read()
setup(
    name='PysaCoolCli',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.0.1',
    install_requires=[
        # TODO add other dependencies here
    ],
    package_dir={'':'src'},
    py_modules=["PysaCoolCli"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
