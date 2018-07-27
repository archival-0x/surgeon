#!/usr/bin/env python2

import os
import argparse
import ast

DEBUG = False

NODE_TYPES = {
    ast.ClassDef: 'Class',
    ast.FunctionDef: 'Function/Method',
    ast.Module: 'Module'
}

def main():

    # initialize our parser
    parser = argparse.ArgumentParser()
    
    # create argument group for required arguments
    required = parser.add_argument_group('required arguments')
    required.add_argument('-f', '--filepath',
                        dest='filepath',
                        help='file to add docstring')
    required.add_argument('-c', '--configuration',
                        dest='configuration',
                        help='configuration file that contains docstring')
    parser.add_argument('-v', '--verbosity',
                        dest='verbosity',
                        action='store_true',
                        help='if set, more verbose outputs will be printed')
    parser.add_argument('-a', '--append-changes',
                        dest='append',
                        action='store_true',
                        help='if set, changes are saved into original source')

    # parse arguments
    args = parser.parse_args()

    # turn on DEBUG if verbosity flag is set
    DEBUG = args.verbosity   
 
    # check for required arguments
    man_options = ['filepath', 'configuration']
    for m in man_options:
        if not args.__dict__[m]:
            parser.print_help()
            return 1
    
    # check if filepath exists and is a file
    if not os.path.isfile(args.filepath):
        print("File doesn't exist. Exiting.")
        return 1
  
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
        print("File contains a syntatical error. Fix before running again")
        return 1

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
                if DEBUG:
                    print("\nFound node line no. with no docstring: {}".format(lineno))
                no_docstring_lines.append(lineno)
            
            # if debug mode is on, print out nodes with docstrings
            elif DEBUG and docstring is not None:
                print("\n\n{}".format(node.name))
                print("------------------------------")
                print("Available Docstring:\n\"{}\"".format(docstring)) 
             
    # if debug mode on, print out how many nodes with no docstrings 
    if DEBUG:
        print("\n\n{} nodes have no docstrings." \
              .format(len(no_docstring_lines)))

    # re-open file, this time, store as buffer for format purposes
    # TODO: improve ??
    with open(args.filepath, 'r') as buf_file:
        buf = buf_file.readlines()

    # inject our docstring template into the code, incrementing a counter.
    # since an insert() call increases the total line count, each lineno has
    # to keep up as well
    i = 0
    for line in no_docstring_lines:
        buf.insert(line + i, template)
        i += 1

    # if debug mode on, print out final formatted code with docstrings
    if DEBUG:
        print("\n\n====================================")
        print("Final docstring-linted code:\n")
        print("".join(buf))

    # if flag is set, merge our docstring-linted changes into our original source
    if args.append:
        with open(args.filepath, 'w') as f_write:
            f_write.write("".join(buf))

    print("\nSuccess! Added docstrings to code")
    return 0

if __name__ == "__main__":
    main()
