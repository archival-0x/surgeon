from setuptools import setup, find_packages

NAME = "pysurgeon"
VERSION = "0.1.0"
DESC = "Surgically implant Python docstrings within source code"

REPO = "https://github.com/ex0dus-0x/pysurgeon"

setup(
    name = NAME,
    version = VERSION,
    author = "Alan <ex0dus@codemuch.tech>",
    description = DESC,
    url = REPO,
    download_url = '{}/archive/v{}'.format(REPO, VERSION),
    packages = find_packages(exclude=('tests',)),
    entry_points = {
        'console_scripts': [
            'pysurgeon=src.pysurgeon:main'
        ],
    }
)
