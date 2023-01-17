#!/usr/bin/env python
import os, sys, glob
from yet_agavestorm import tsklib


def main():
    argv = sys.argv;
    argv.pop(0); # remove first element, pointing to script itself
    if len(argv) != 1 :
        print("""
        Usage:
            yet drop %taskId%   - completely remove single task with specified id
        Example:
            yet drop 3
            """)
        exit(1);
        pass;
    id = argv[0]
    file = tsklib.getTaskFilenameById(id)
    print("Deleting task "+file+" .. ", end="")
    os.remove(file)
    print("done")
    pass

if __name__=="__main__":
    main()
    pass

