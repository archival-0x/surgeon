from setuptools import setup, find_packages


# setup.py constants
NAME = "pysurgeon"
VERSION = "0.1.0"
DESC = "Surgically implant Python docstrings within source code"

REPO = "https://github.com/ex0dus-0x/pysurgeon"


# main setup script
setup(
    name = NAME,
    version = VERSION,
    author = "Alan <ex0dus@codemuch.tech>",
    description = DESC,
    url = REPO,
    download_url = '{}/archive/v{}'.format(REPO, VERSION),
    packages = find_packages(exclude=('tests',)),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License:: OSI Approved :: MIT License",
        "Operating System :: Linux"
    ),
    entry_points = {
        'console_scripts': [
            'pysurgeon=src.pysurgeon:main'
        ],
    }
)
