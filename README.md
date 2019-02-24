# surgeon

Surgically implant docstrings (template, for now) into Python source code

## intro

__surgeon__ "surgically implants" docstrings into Python source code by breaking
down the source into an _abstract syntax tree_, identify nodes that don't have a
docstring, and then injecting it based on a user-supplied template.

## install

```
$ pip install pysugeon --user
```

or if you choose to manually:

```
$ python setup.py install
```

## usage

```
usage: surgeon [-h] -f FILEPATH -c CONFIGURATION [-d] [-a]

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           if set, verbose debug outputs will be printed
  -a, --append-changes  if set, changes are saved into original source

required arguments:
  -f FILEPATH, --filepath FILEPATH
                        file to add docstring
  -c CONFIGURATION, --configuration CONFIGURATION
                        configuration file that contains docstring
```

## example

This example implants a template docstring from `my_template.txt` into
a test file:

```
$ surgeon -f tests/test_basic_lint.py -c my_template.txt -a
```

## license

[mit](https://codemuch.tech/license.txt)
