#!/usr/bin/env python3
import os
import logging
import argparse
import ast

logger = logging.getLogger(__name__)

# define node types to implant docstrings
NODE_TYPES = {
    ast.ClassDef: 'Class',
    ast.FunctionDef: 'Function/Method',
    ast.Module: 'Module'
}


def main():
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group('required arguments')

    # required arguments
    required.add_argument('-f', '--filepath',
                        dest='filepath', required=True,
                        help='file to add docstring')
    required.add_argument('-c', '--configuration',
                        dest='configuration', required=True,
                        help='configuration file that contains docstring')

    # other options
    parser.add_argument('-d', '--debug',
                        action='store_true',
                        dest='debug', required=False,
                        help='if set, verbose debug outputs will be printed')
    parser.add_argument('-a', '--append-changes',
                        action='store_true',
                        dest='append', required=False,
                        help='if set, changes are saved into original source')

    # parse arguments
    args = parser.parse_args()

    # log if debug flag is set
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # check for required arguments
    man_options = ['filepath', 'configuration']
    for m in man_options:
        if not args.__dict__[m]:
            parser.print_help()
            return 1

    # check if filepath exists and is a file
    if not os.path.isfile(args.filepath):
        raise RuntimeError("File doesn't exist. Exiting.")

    # open file for reading and store contents
    with open(args.filepath, 'r') as f:
        source = f.read()

    # open configuration path for docstring template
    with open(args.configuration, 'r') as f:
        template = f.read()

    # parse as AST tree
    try:
        code = ast.parse(source)
    except SyntaxError:
        raise RuntimeError("File contains a syntatical error. Fix before running again")

    # go for each node over the AST
    no_docstring_lines = []
    for node in code.body:

        # check if module, class, and/or function
        if isinstance(node, tuple(NODE_TYPES)):

            # if there is no docstring, get the line number
            # since we can't mutate docstring code
            docstring = ast.get_docstring(node)

            if docstring is None:
                lineno = getattr(node, 'lineno', None)
                logger.debug(f"Found node line no. with no docstring: {lineno}")
                no_docstring_lines.append(lineno)

            else:
                logger.debug(f"{node.name}: {docstring}")

    # if debug mode on, print out how many nodes with no docstrings
    logger.debug(f"{len(no_docstring_lines)} nodes have no docstrings.")

    # re-open file, this time, store as buffer for format purposes
    with open(args.filepath, 'r') as buf_file:
        buf = buf_file.readlines()

    # inject our docstring template into the code, incrementing a counter.
    # since an insert() call increases the total line count, each lineno has
    # to keep up as well
    i = 0
    for line in no_docstring_lines:
        buf.insert(line + i, template)
        i += 1

    # print out final formatted code with docstrings
    print(" ".join(buf))
    
    # if flag is set, merge our docstring-linted changes into our original source
    if args.append:
        with open(args.filepath, 'w') as f_write:
            f_write.write("".join(buf))

    return 0

if __name__ == "__main__":
    main()
