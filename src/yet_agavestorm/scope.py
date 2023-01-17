#!/usr/bin/env python
import os, sys, glob, yaml, subprocess, datetime
from yet_agavestorm import tsklib
from pathlib import Path

def main():
    argv = sys.argv;
    argv.pop(0); # remove first element, pointing to script itself
    if len(argv) == 0 :
        print("""
        Usage:
            yet scope reset
            yet scope context contextName
            yet scope project projectName
            yet scope list
            """)
        exit(1);
        pass;

    command = argv[0]
    scope = tsklib.loadScope();
    if command == "list":
        for key in scope:
            print("Name: TSK_"+key.upper()+" = "+scope[key] )
        exit(0)
        pass

    if command == "reset":
        tsklib.saveScope({})
        exit(0)
        pass

    if not command in scope.keys():
        print("Unexpected parameter "+command)
        exit(1)
        pass

    argv.pop(0)
    value = " ".join(argv)
    scope[command] = value
    tsklib.saveScope( scope )
    pass

if __name__=="__main__":
    main()
    pass
