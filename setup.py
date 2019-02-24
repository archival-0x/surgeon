from setuptools import setup, find_packages


# setup.py constants
NAME = "surgeon"
VERSION = "0.2.0"
DESC = "Surgically implant Python docstrings within source code"
REPO = "https://github.com/ex0dus-0x/surgeon"


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
        "Programming Language :: Python :: 3",
        "License:: OSI Approved :: MIT License",
        "Operating System :: Linux"
    ),
    entry_points = {
        'console_scripts': [
            'surgeon=surgeon.surgeon:main'
        ],
    }
)
