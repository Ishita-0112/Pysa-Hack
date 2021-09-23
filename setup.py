from setuptools import setup, find_packages

with open("README.md", "r") as fh: 
    long_description = fh.read()

setup(
    name='PysaCoolCli',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # TODO add other dependencies here
        'Click',
        'Django',
    ],
    entry_points='''
        [console_scripts]
        PysaCoolCli=PysaCoolCli.commands:PysaCoolCli
    ''',
)
