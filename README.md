# pysurgeon

Surgically implant docstrings (template, for now) into Python source code

## Introduction

__pysurgeon__ "surgically implants" docstrings into Python source code by breaking
down the source into an _abstract syntax tree_, identify nodes that don't have a
docstring, and then injecting it based on a user-supplied template.

## Installation

```
$ python setup.py install
```

## Usage

```
usage: pysurgeon.py [-h] [-f FILEPATH] [-c CONFIGURATION] [-v] [-a]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbosity       if set, more verbose outputs will be printed
  -a, --append-changes  if set, changes are saved into original source

required arguments:
  -f FILEPATH, --filepath FILEPATH      
                        file to add docstring
  -c CONFIGURATION, --configuration CONFIGURATION
                        configuration file that contains docstring
```

### See how it works:

```
pysurgeon -f tests/test_basic_lint.py -c my_template.txt -a
```

## TODO

- [ ] Regex parsing for automatic docstring text generation
- [ ] Better formatting / text alignment
- [ ] Better insertion for template within text buffer (C? but a little overkill)
